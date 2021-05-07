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
  return await axios.get(apiUrl + "contexts");
};

export const DeleteContext = async (identifier_hash: string) => {
  return await axios.delete(apiUrl + "context/" + identifier_hash);
};

export const CreateSummaryDocument = async (identifier_hash: string) => {
  return await axios.put(apiUrl + "word_document/" + identifier_hash);
};
