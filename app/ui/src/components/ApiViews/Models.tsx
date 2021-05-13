// generated models
export declare interface SearchContext {
  search_request: Searchrequest;
  search_result_pages: Searchresultpage[];
  count_of_search_results: number;
  exec_state_name: string;
  exec_state_value: number;
  exec_state_issues: string;
  word_document_state_name: string;
  word_document_state_value: number;
  word_document_info: string;
}

export declare interface Searchresultpage {
  http_request_parameters: Httprequestparameters;
  search_response_file: string;
  search_results: Searchresult[];
}

export declare interface Searchresult {
  authors: string;
  publication: string;
  hash: string;
  title: string;
  site_url: string;
  abstract: string;
  citations: number;
  related: string;
  pdf_filepath: string;
  pdf_filename: string;
  pdf_url: string;
  pdf_status: string;
  pdf_status_info: string;
  pdf_filetime: string;
}

interface Httprequestparameters {
  headers: Headers;
  page: number;
  url: string;
}

interface Headers {
  "User-Agent": string;
}

interface Searchrequest {
  source_name: string;
  terms: string[];
  terms_string: string;
  terms_hash: string;
  identifier: string;
  identifier_hash: string;
}

// non-generated models

export type UpdateContextsFn = (contexts: SearchContext[]) => void;

export declare interface ApiResponse {
  responseStatus: number;
  responseStatusText: string;
  searchContexts: SearchContext[];
  filters: string[];
  update: UpdateContextsFn;
}
