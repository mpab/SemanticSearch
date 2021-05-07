import React from "react";
import { useToasts } from "react-toast-notifications";
import { SortContextsBySearchTerms, GetSourceImageTextFragment } from "..";

import {
  CreateContext,
  CreateSummaryDocument,
  DeleteContext,
  docUrl,
  ExecuteContext,
  GetContexts,
} from "../../../Api";
import {
  ButtonProps,
  ChildPolicy,
  InputProps,
  LabelProps,
  ModalDialogPopupButtonProps,
  UrlProps,
} from "../../CommonControls/Models";
import { Control } from "../../CommonControls/ParentControls";
import { _classNames } from "../../CommonControls/_classNames";
import {
  BreadConvert,
  FailBread,
  SuccessBread,
  WarningBread,
} from "../../Toast";
import { StringUtil } from "../../Utilities";
import { ApiResponse, SearchContext } from "../Models";

// TODO
// word link
const RenderDocLink = (apiResponse: ApiResponse, context: SearchContext) => {
  const { addToast } = useToasts();

  const update = async () => {
    await GetContexts().then((response) => {
      if (response.status === 200) {
        const collection = response.data as SearchContext[];
        const sorted = SortContextsBySearchTerms(collection);
        apiResponse.update(sorted);
      }
    });
  };

  const onClick = async () => {
    await CreateSummaryDocument(context.search_request.identifier_hash)
      .then((response) => {
        if (response.status === 200) {
          const p = BreadConvert(SuccessBread([response.data]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
          update();
          return;
        }
        const p = BreadConvert(WarningBread([response.data]));
        addToast(p.content, {
          appearance: p.appearance,
          autoDismiss: p.autoDismiss,
        });
      })
      .catch((err) => {
        const p = BreadConvert(FailBread([err]));
        addToast(p.content, {
          appearance: p.appearance,
          autoDismiss: p.autoDismiss,
        });
      });
  };

  if (context.exec_state_value === 0) {
    if (context.word_document_state_value === 0) {
      return Control(
        UrlProps({
          image: "",
          title: "open",
          link: docUrl + context.word_document_info,
          subtitles: [""],
        })
      );
    }

    if (context.word_document_state_value === 1) {
      return Control(
        ButtonProps({
          image: "",
          title: "generate",
          onClick: onClick,
        })
      );
    }

    return Control(
      LabelProps({
        image: "",
        title: "error",
        getValue: () => {
          return context.word_document_info;
        },
      })
    );
  }

  return <></>;
};

const RenderBody = (apiResponse: ApiResponse): React.ReactElement => {
  const { addToast } = useToasts();

  if (apiResponse.responseStatus !== 200) {
    return (
      <div className="text-3xl font-bold text-red-600">
        API ERROR {apiResponse.responseStatus}
      </div>
    );
  }

  const statusFriendlyName = (context: SearchContext) => {
    return context.exec_state_name.slice(-context.exec_state_name.length + 7);
  };

  const runActionButton = (context: SearchContext) => {
    const update = async () => {
      await GetContexts().then((response) => {
        if (response.status === 200) {
          const collection = response.data as SearchContext[];
          const sorted = SortContextsBySearchTerms(collection);
          apiResponse.update(sorted);
        }
      });
    };

    const onClick = async () => {
      await ExecuteContext(context.search_request.identifier_hash)
        .then((response) => {
          if (response.status === 200) {
            const p = BreadConvert(SuccessBread([response.data]));
            addToast(p.content, {
              appearance: p.appearance,
              autoDismiss: p.autoDismiss,
            });
            update();
            return;
          }
          const p = BreadConvert(WarningBread([response.data]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        })
        .catch((err) => {
          const p = BreadConvert(FailBread([err]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        });
    };

    if (context.exec_state_value > 0) {
      const props = ButtonProps({
        title: "run",
        image: "",
        onClick: onClick,
      });
      return Control(props);
    }

    return <></>;
  };

  const deleteActionButton = (context: SearchContext) => {
    const update = async () => {
      await GetContexts().then((response) => {
        if (response.status === 200) {
          const collection = response.data as SearchContext[];
          const sorted = SortContextsBySearchTerms(collection);
          apiResponse.update(sorted);
        }
      });
    };

    const onClick = async () => {
      await DeleteContext(context.search_request.identifier_hash)
        .then((response) => {
          if (response.status === 200) {
            const p = BreadConvert(SuccessBread(["delete", response.data]));
            addToast(p.content, {
              appearance: p.appearance,
              autoDismiss: p.autoDismiss,
            });
            update();
            return;
          }
          const p = BreadConvert(WarningBread(["delete", response.data]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        })
        .catch((err) => {
          const p = BreadConvert(FailBread(["delete", err]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        });
    };

    const props = ButtonProps({
      title: "delete",
      image: "",
      onClick: onClick,
    });

    return Control(props);
  };

  const statusProps = (context: SearchContext) => {
    return ModalDialogPopupButtonProps({
      title: statusFriendlyName(context),
      image: "",
      header: "",
      footer: "",
      policy: ChildPolicy.NeverCloseIfAnyClicked,
      children: [
        LabelProps({
          title: "Execution State",
          getValue: () => {
            return context.exec_state_name;
          },
        }),
        LabelProps({
          title: "Execution State Value",
          getValue: () => {
            return context.exec_state_value + "";
          },
        }),
        LabelProps({
          title: "Execution State Issues",
          getValue: () => {
            return context.exec_state_issues + "";
          },
        }),
      ],
    });
  };

  return (
    <tbody className="bg-white divide-y divide-gray-200">
      {apiResponse.searchContexts.map((context, index) => (
        <>
          <tr>
            <td className="px-6 py-4 whitespace-nowrap">
              {StringUtil.arrayToString(context.search_request.terms)}
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              {GetSourceImageTextFragment(context)}
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              {Control(statusProps(context))}
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              {runActionButton(context)}
              {deleteActionButton(context)}
            </td>
            <td className="px-6 py-4 whitespace-nowrap">
              {RenderDocLink(apiResponse, context)}
            </td>
          </tr>
        </>
      ))}
    </tbody>
  );
};

export const RenderManageSearchesView = (
  apiResponse: ApiResponse
): React.ReactElement => {
  const { addToast } = useToasts();

  const update = async () => {
    await GetContexts().then((response) => {
      if (response.status === 200) {
        const collection = response.data as SearchContext[];
        const sorted = SortContextsBySearchTerms(collection);
        apiResponse.update(sorted);
      }
    });
  };

  const NewSearchControl = () => {
    var terms: string = "";
    const handleOnSubmit = async () => {
      await CreateContext(terms)
        .then((response) => {
          if (response.status === 200) {
            const p = BreadConvert(SuccessBread(["create", response.data]));
            addToast(p.content, {
              appearance: p.appearance,
              autoDismiss: p.autoDismiss,
            });
            update();
            return;
          }
          const p = BreadConvert(WarningBread(["create", response.data]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        })
        .catch((err) => {
          const p = BreadConvert(FailBread(["create", err]));
          addToast(p.content, {
            appearance: p.appearance,
            autoDismiss: p.autoDismiss,
          });
        });
    };

    const props = InputProps({
      title: "New Search",
      getValue: () => {
        return "";
      },
      onChange: (e: React.ChangeEvent<HTMLInputElement>) => {
        //console.log("Add Term: " + e.target.value);
        terms = e.target.value;
      },

      onSubmit: (terms: string) => {
        handleOnSubmit();
      },

      className: _classNames.purplePlainFrame,
    });

    return Control(props);
  };

  return (
    <>
      <div className="flex justify-left">
        <NewSearchControl />
      </div>
      <div className="flex flex-col">
        <div className="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
            <div className="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Search Identifier
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Source
                    </th>

                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Status
                    </th>

                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Action
                    </th>

                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Summary Document
                    </th>

                    <th scope="col" className="relative px-6 py-3">
                      <span className="sr-only">Edit</span>
                    </th>
                  </tr>
                </thead>
                {RenderBody(apiResponse)}
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
