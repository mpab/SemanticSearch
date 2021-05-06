import { ReactElement } from "react";
import { ControlProps } from "./Models";
import { _classNames } from "./_classNames";

interface ExtendedControlProps {
  common: ControlProps;
  subTitleClassName: string;
}

export const ExLayoutTitleWithValue: React.FC<ExtendedControlProps> = (
  props
): ReactElement => {
  return (
    <>
      {props.common.title ? (
        <>
          <label className={_classNames.invisibleFrameWithBorder}>
            {props.common.title}
          </label>
          {props.common.getValue ? (
            <label className={props.common.className}>
              {props.common.getValue()}
            </label>
          ) : (
            <></>
          )}
        </>
      ) : (
        <></>
      )}
    </>
  );
};

export const LayoutTitleWithValue = (props: ControlProps): ReactElement => {
  return (
    <ExLayoutTitleWithValue
      {...{ common: props, subTitleClassName: _classNames.plainText }}
    />
  );
};

export const LayoutTitleWithHoverSubtitles = (
  props: ControlProps
): ReactElement => {
  return (
    <ExLayoutTitleWithSubtitles
      {...{ common: props, subTitleClassName: _classNames.hoverText }}
    />
  );
};

export const LayoutTitleWithPlainSubtitles = (
  props: ControlProps
): ReactElement => {
  return (
    <ExLayoutTitleWithSubtitles
      {...{ common: props, subTitleClassName: _classNames.plainText }}
    />
  );
};

export const ExLayoutTitleWithSubtitles: React.FC<ExtendedControlProps> = (
  props
): ReactElement => {
  return (
    <>
      {props.common.title ? (
        <div className="mt-0 ml-4">
          <div>{props.common.title}</div>
          {props.common.subtitles?.map((item, index) => {
            return (
              <p key={index} className={props.subTitleClassName}>
                {item}
              </p>
            );
          })}
        </div>
      ) : (
        <></>
      )}
    </>
  );
};

export const LayoutImage: React.FC<ControlProps> = (props): ReactElement => {
  return (
    <>
      {props.image ? (
        <img className={_classNames.image} src={props.image} alt="" />
      ) : (
        <></>
      )}
    </>
  );
};

export const LayoutImage2: React.FC<ControlProps> = (props): ReactElement => {
  return (
    <>
      {props.image ? (
        <div className={props.className}>
          <img className={_classNames.image} src={props.image} alt="" />
        </div>
      ) : (
        <></>
      )}
    </>
  );
};
