import React from "react";
import { GetContexts } from "../../Api";
import { StringUtil } from "../Utilities";
import { RenderManageSearchesView } from "./ManageSearchesView/Render";
import { ApiResponse, SearchContext } from "./Models";
import { RenderSearchResultsView } from "./SearchResultsView/Render";

export const SortContextsBySearchTerms = (
  contexts: SearchContext[]
): SearchContext[] => {
  const sorted: SearchContext[] = contexts.sort((a, b) => {
    const a_terms = StringUtil.arrayToString(a.search_request.terms);
    const b_terms = StringUtil.arrayToString(b.search_request.terms);
    if (a_terms > b_terms) return 1;
    if (a_terms < b_terms) return -1;
    if (a.search_request.source_name > b.search_request.source_name) return 1;
    if (a.search_request.source_name < b.search_request.source_name) return -1;
    return 0;
  });
  return sorted;
};

const sortSearches = (searches: string[]): string[] => {
  const sorted: string[] = searches.sort((a, b) => {
    if (a > b) return 1;
    if (a < b) return -1;
    return 0;
  });
  return sorted;
};

export const GetSourceImageTextFragment = (context: SearchContext) => {
  return (
    <>
      <div className="flex-shrink-0 h-10 w-10">
        {context.search_request.source_name === "arxiv" ? (
          <img className="h-10 w-10" src="./cornell-logo-red.jpg" alt="" />
        ) : (
          <img className="h-10 w-10" src="./google-scholar-logo.png" alt="" />
        )}
      </div>
      <div className="text-sm font-medium text-gray-900">
        {context.search_request.source_name}
      </div>
    </>
  );
};

export const getSearches = (
  contexts: SearchContext[],
  init: string = ""
): string[] => {
  const arr: string[] = init === "" ? [] : [init];
  for (var i = 0; i !== contexts.length; ++i) {
    const terms = StringUtil.arrayToString(contexts[i].search_request.terms);
    if (!arr.includes(terms)) {
      arr.push(terms);
    }
  }
  return sortSearches(arr);
};

const GetData = (initSearch: string = ""): ApiResponse => {
  const [contexts, setContexts] = React.useState<SearchContext[]>([]);
  const [status, setStatus] = React.useState<number>(200);
  const [statusText, setStatusText] = React.useState<string>("");

  React.useEffect(() => {
    let isMounted = true; // https://stackoverflow.com/questions/53949393/cant-perform-a-react-state-update-on-an-unmounted-component
    GetContexts()
      .then((response) => {
        if (isMounted) {
          if (response.status === 200) {
            const collection = response.data as SearchContext[];
            const sorted = SortContextsBySearchTerms(collection);
            setContexts(sorted);
          } else {
            setContexts([]);
          }
          setStatus(response.status);
          setStatusText(response.statusText);
        }
      })
      .catch((err) => {
        if (err.response) {
          setStatus(err.response.status);
          setStatusText(err.response.statusText);
        } else if (err.request) {
          setStatus(err.request.status);
          setStatusText(err.request.statusText);
        } else {
          setStatus(-1);
          setStatusText("unexpected error");
        }
        setContexts([]);
        console.exception(err);
      });
    return () => {
      isMounted = false;
    };
  }, []);

  const [filters, setFilters] = React.useState<string[]>(
    getSearches(contexts, "*")
  );

  React.useEffect(() => {
    let isMounted = true; // https://stackoverflow.com/questions/53949393/cant-perform-a-react-state-update-on-an-unmounted-component
    if (isMounted) {
      setFilters(getSearches(contexts, initSearch));
    }
    return () => {
      isMounted = false;
    };
  }, [contexts, initSearch]);

  const updateContexts = (contexts: SearchContext[]) => {
    setContexts(contexts);
  };

  return {
    responseStatus: status,
    responseStatusText: statusText,
    searchContexts: contexts,
    filters: filters,
    update: updateContexts,
  };
};

export const SearchResultsView = (): React.ReactElement => {
  const apiResponse: ApiResponse = GetData("*");
  return RenderSearchResultsView(apiResponse);
};

export const ManageSearchesView = (): React.ReactElement => {
  const apiResponse: ApiResponse = GetData();
  return RenderManageSearchesView(apiResponse);
};
