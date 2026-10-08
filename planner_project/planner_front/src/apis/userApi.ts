import axios from "axios";

// 서버 경로
// 127.0.0.1 == localhost
const url = "http://127.0.0.1:8000/user";

export type User = {
  email: string;
  password: string;
  events?: Event[];
};

export const postNewUser = async (email: string, password: string) => {
  const response = await axios.post(`${url}/signup`, {
    email,
    password,
    events: [],
  });
  return response.data;
};

export const signin = async (email: string, password: string) => {
  const response = await axios.post(`${url}/signin`, {
    email,
    password,
  });
  return response.data;
};
