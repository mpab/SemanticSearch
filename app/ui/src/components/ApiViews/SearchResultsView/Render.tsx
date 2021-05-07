import React from "react";
import { GetSourceImageTextFragment } from "..";
import { pdfUrl } from "../../../Api";
import {
  ChildPolicy,
  LabelProps,
  ModalDialogPopupButtonProps,
  TextSelectProps,
  UrlProps,
} from "../../CommonControls/Models";
import { Control } from "../../CommonControls/ParentControls";
import { _classNames } from "../../CommonControls/_classNames";
import { StringUtil } from "../../Utilities";
import {
  ApiResponse,
  SearchContext,
  Searchresult,
  Searchresultpage,
} from "../Models";

const buildFilteredApiResponse = (
  apiResponse: ApiResponse,
  filter: string
): ApiResponse => {
  const filteredSearchContexts: SearchContext[] = [];

  if (filter === "*" || filter === "") {
    return apiResponse; // NOP
  }

  for (var i = 0; i !== apiResponse.searchContexts.length; ++i) {
    const context: SearchContext = apiResponse.searchContexts[i];

    const termsCss = StringUtil.arrayToString(context.search_request.terms);

    if (filter === termsCss) {
      filteredSearchContexts.push(context);
      continue;
    }
  }

  apiResponse.searchContexts = filteredSearchContexts;

  return apiResponse;
};

const makeCountsFeatureUrl = (
  context: SearchContext,
  searchresult: Searchresult
) => {
  return (
    "http://localhost:5000/feature/counts/" +
    context.search_request.identifier_hash +
    "/" +
    searchresult.hash
  );
};

const makeExtractFeatureUrl = (
  context: SearchContext,
  searchresult: Searchresult
) => {
  return (
    "http://localhost:5000/feature/extract/" +
    context.search_request.identifier_hash +
    "/" +
    searchresult.hash
  );
};

const makeTagsFeatureUrl = (
  context: SearchContext,
  searchresult: Searchresult
) => {
  return (
    "http://localhost:5000/feature/tags/" +
    context.search_request.identifier_hash +
    "/" +
    searchresult.hash
  );
};

const makeTokensFeatureUrl = (
  context: SearchContext,
  searchresult: Searchresult
) => {
  return (
    "http://localhost:5000/feature/tokens/" +
    context.search_request.identifier_hash +
    "/" +
    searchresult.hash
  );
};

const makeTokensGraphFeatureUrl = (
  context: SearchContext,
  searchresult: Searchresult
) => {
  return (
    "http://localhost:5000/feature/tokens_graph/" +
    context.search_request.identifier_hash +
    "/" +
    searchresult.hash
  );
};

const Actions = (context: SearchContext, searchresult: Searchresult) => {
  if (searchresult.pdf_status === "validated") {
    return Control(
      ModalDialogPopupButtonProps({
        title: "documents",
        header: "Select Action",
        footer: "",
        image: "",
        policy: ChildPolicy.CloseIfAnyClicked,
        className: _classNames.purplePlainFrame,
        children: [
          LabelProps({
            title: "Title",
            getValue: () => {
              return searchresult.title;
            },
          }),
          UrlProps({
            image: "",
            title: "view research paper",
            link: pdfUrl + searchresult.pdf_filename,
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
          UrlProps({
            image: "",
            title: "features: view token counts",
            link: makeCountsFeatureUrl(context, searchresult),
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
          UrlProps({
            image: "",
            title: "features: view text extract",
            link: makeExtractFeatureUrl(context, searchresult),
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
          UrlProps({
            image: "",
            title: "features: view tag mappings",
            link: makeTagsFeatureUrl(context, searchresult),
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
          UrlProps({
            image: "",
            title: "features: view tokens",
            link: makeTokensFeatureUrl(context, searchresult),
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
          UrlProps({
            image: "",
            title: "features: view tokens graph",
            link: makeTokensGraphFeatureUrl(context, searchresult),
            subtitles: [""],
            className: _classNames.purpleHoverFrame,
          }),
        ],
      })
    );
  }

  return <></>;
};

const shorten = (text: string, maxLen: number = 64) => {
  if (text.length >= maxLen) {
    return text.slice(0, maxLen / 2 - 1) + ".." + text.slice(-maxLen / 2 - 1);
  }
  return text;
};

const ResultDetailsButton = (searchresult: Searchresult, key: number) => {
  const children = [
    LabelProps({
      title: "Title",
      getValue: () => {
        return searchresult.title;
      },
    }),
    LabelProps({
      title: "Authors",
      getValue: () => {
        return searchresult.authors;
      },
    }),
    LabelProps({
      title: "Publication",
      getValue: () => {
        return searchresult.publication;
      },
    }),
    UrlProps({
      image: "",
      title: searchresult.site_url,
      link: searchresult.site_url,
      subtitles: [],
    }),
    LabelProps({
      title: "Citations",
      getValue: () => {
        return searchresult.citations + "";
      },
    }),
  ];

  const props = ModalDialogPopupButtonProps({
    title: shorten(searchresult.title),
    image: "",
    header: "Result Details",
    footer: "",
    policy: ChildPolicy.NeverCloseIfAnyClicked,
    children: children,
    className: _classNames.purplePlainFrame,
  });

  return Control(props);
};

const RenderPdfStatus = (searchresult: Searchresult) => {
  if (searchresult.pdf_status === "not processed") {
    return (
      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
        not processed
      </span>
    );
  }

  if (searchresult.pdf_status === "validated") {
    return (
      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
        validated
      </span>
    );
  }

  if (searchresult.pdf_status === "downloaded") {
    return (
      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
        downloaded, not validated
      </span>
    );
  }

  if (searchresult.pdf_status === "error") {
    return (
      <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
        {searchresult.pdf_status_info}
      </span>
    );
  }

  return (
    <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-100 text-yellow-800">
      unknown status
    </span>
  );
};

const Status = (searchresult: Searchresult, key: number) => {
  return <div>{RenderPdfStatus(searchresult)}</div>;
};

const RenderGridLine = (
  context: SearchContext,
  contextIndex: number,
  searchResultPage: Searchresultpage,
  searchResultPageIndex: number,
  searchResult: Searchresult,
  searchResultIndex: number
) => {
  const checkboxChange = () => {};
  return (
    <tr>
      <td className="px-6 py-4 whitespace-nowrap">
        <label>
          <input
            className="mr-2"
            checked={false}
            defaultValue="false"
            onChange={checkboxChange}
            type="checkbox"
          />
        </label>
      </td>
      <td className="px-6 py-4 whitespace-nowrap">
        <div className="flex items-center">
          <div className="ml-4">
            <div className="text-sm font-medium text-gray-900">
              Id: {context.search_request.identifier_hash}
            </div>
            <div className="text-sm font-medium text-gray-900">
              {context.search_request.terms_hash}
            </div>
            <div className="text-sm text-gray-500">
              {StringUtil.arrayToString(context.search_request.terms)}
            </div>
          </div>
        </div>
      </td>
      <td className="px-6 py-4 whitespace-nowrap">
        {GetSourceImageTextFragment(context)}
      </td>

      <td className="px-6 py-4 whitespace-nowrap">{searchResult.citations}</td>

      <td className="px-6 py-4 whitespace-nowrap">
        {ResultDetailsButton(searchResult, searchResultIndex)}
      </td>

      <td className="px-6 py-4 whitespace-nowrap">
        {Status(searchResult, searchResultIndex)}
      </td>

      <td className="px-6 py-4 whitespace-nowrap">
        {Actions(context, searchResult)}
      </td>
    </tr>
  );
};

const RenderBody = (apiResponse: ApiResponse): React.ReactElement => {
  if (apiResponse.responseStatus !== 200) {
    return (
      <div className="text-3xl font-bold text-red-600">
        API ERROR {apiResponse.responseStatus}
      </div>
    );
  }

  return (
    <tbody className="bg-white divide-y divide-gray-200">
      {apiResponse.searchContexts.map((context, contextKey) => {
        return context.search_result_pages.map(
          (searchResultPage, searchResultPageIndex) => {
            return searchResultPage.search_results.map(
              (searchResult, searchResultIndex) => {
                return RenderGridLine(
                  context,
                  contextKey,
                  searchResultPage,
                  searchResultPageIndex,
                  searchResult,
                  searchResultIndex
                );
              }
            );
          }
        );
      })}
    </tbody>
  );
};

export const RenderSearchResultsView = (
  apiResponse: ApiResponse
): React.ReactElement => {
  const [
    filteredApiResponse,
    setFilteredApiResponse,
  ] = React.useState<ApiResponse>(apiResponse);

  const [filter, setFilter] = React.useState<string>("*");

  const FilterControl = () => {
    const props = TextSelectProps({
      title: "Filter",
      image: "",
      className:
        "text-left text-xs font-medium text-gray-500 uppercase tracking-wider",
      onSelect: (e: React.ChangeEvent<HTMLSelectElement>) => {
        setFilter(e.target.value);
        setFilteredApiResponse(
          buildFilteredApiResponse(apiResponse, e.target.value)
        );
        //console.log("SelectControl.onSelect: " + e.target.value);
      },
      getValues: () => {
        return apiResponse.filters;
      },
      getValue: () => {
        //console.log("SelectControl.getValue: " + filter);
        return filter;
      },
    });

    return Control(props);
  };

  return (
    <>
      <div className="flex justify-left">
        <FilterControl />
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
                      Select
                    </th>
                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Search Terms
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
                      Citations
                    </th>

                    <th
                      scope="col"
                      className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                    >
                      Result Details
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
                      Actions
                    </th>

                    <th scope="col" className="relative px-6 py-3">
                      <span className="sr-only">Edit</span>
                    </th>
                  </tr>
                </thead>
                {RenderBody(filteredApiResponse)}
              </table>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
