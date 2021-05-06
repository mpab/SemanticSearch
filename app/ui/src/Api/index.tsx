import axios from "axios";

const apiUrl = new URL("http://localhost:5000/api/");
export const pdfUrl = new URL("http://localhost:5000/pdf/");
export const docUrl = new URL("http://localhost:5000/doc/");

export const CreateContext = async (terms: string) => {
  return await axios.put(apiUrl + "context/" + terms);
};

export const ExecuteContext = async (identifier_hash: string) => {
  return await axios.post(apiUrl + "context/" + identifier_hash);
};

export const GetContexts = async () => {
  return await axios.get(apiUrl + "context");
};

export const GetCountsFeatureDocument = async (
  identifier_hash: string,
  result_hash: string
) => {
  return await axios.get(
    apiUrl + "feature/counts/" + identifier_hash + "/" + result_hash
  );
};

export const GetExtractFeatureDocument = async (
  identifier_hash: string,
  result_hash: string
) => {
  return await axios.get(
    apiUrl + "feature/extract/" + identifier_hash + "/" + result_hash
  );
};

export const GetTagsFeatureDocument = async (
  identifier_hash: string,
  result_hash: string
) => {
  return await axios.get(
    apiUrl + "feature/tags/" + identifier_hash + "/" + result_hash
  );
};

export const GetTokensFeatureDocument = async (
  identifier_hash: string,
  result_hash: string
) => {
  return await axios.get(
    apiUrl + "feature/tokens/" + identifier_hash + "/" + result_hash
  );
};

export const GetTokensGraphFeatureDocument = async (
  identifier_hash: string,
  result_hash: string
) => {
  return await axios.get(
    apiUrl + "feature/tokens_graph/" + identifier_hash + "/" + result_hash
  );
};

export const DeleteContext = async (identifier_hash: string) => {
  return await axios.delete(apiUrl + "context/" + identifier_hash);
};

export const CreateSummaryDocument = async (identifier_hash: string) => {
  return await axios.put(apiUrl + "word_document/" + identifier_hash);
};
