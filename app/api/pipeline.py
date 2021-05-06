import json
import os

from utilities import JsonEncoder


class Stage:
    def __init__(self, stage_id, in_filepath, out_filepath):
        
        if in_filepath == out_filepath:
            raise Exception('ERROR: "' + in_filepath + ' cannot be the same as "' + out_filepath + '"')

        self.stage_id = stage_id
        self.in_filepath = in_filepath
        self.out_filepath = out_filepath
        self.errors = ''

        if not os.path.exists(self.in_filepath):
            self.errors = 'stage: ' + str(self.stage_id) + 'input file:' + self.in_filepath + 'not found'
        else:
            self.errors = None

    def __str__(self):
        return json.dumps(self, indent=2, cls=JsonEncoder)

    def check_if_output_exists(self):
        
        if os.path.exists(self.out_filepath):
            print ('stage:', self.stage_id, 'output file:', self.out_filepath, 'exists')
            return True

        print ('stage:', self.stage_id, 'output file:', self.out_filepath, 'not found')
        return False

    def raise_error(self, error: str):
        self.errors = 'stage: ' + str(self.stage_id) + ' ' + error
        raise Exception(self.errors)

class PipelineStages:
    def __init__(self, current_stage_id: int, filename: str):
        self.filename = filename
        self.current_stage_id = current_stage_id
        self.stages = {}

    def init_stage(self, in_filepath: str, out_filepath: str) -> Stage:

        stage = self.stages.get(self.current_stage_id)
        if not stage is None:
            raise Exception('ERROR: stage ' + str(self.current_stage_id) + ' is already initialised')

        if self.current_stage_id == 0:
            stage = Stage(self.current_stage_id, in_filepath, out_filepath)
        else:
            stage = Stage(self.current_stage_id, in_filepath, out_filepath)

        self.stages[self.current_stage_id] = stage
        self.current_stage_id = self.current_stage_id + 1    

        return stage

    def find_stage(self, stage_id) -> Stage:
        return self.stages.get(stage_id)

    def get_stage(self) -> Stage:
        return self.stages.get(self.current_stage_id - 1)
    