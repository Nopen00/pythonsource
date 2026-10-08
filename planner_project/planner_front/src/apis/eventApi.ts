// 서버로 데이터 전송, 데이터 가져오기 => fetch(), axios
import axios from "axios";

// 서버 경로
// 127.0.0.1 == localhost
const url = "http://127.0.0.1:8000/event";

export type Event = {
  id?: number;
  title: string;
  image: string;
  description: string;
  tags: string[];
  location: string;
};

// # 전체조회, 수정(put, patch), 삭제, 추가

export const getEvents = async () => {
  const response = await axios.get(`${url}/`);
  return response.data;
};

export const getEvent = async (id: number) => {
  const response = await axios.get(`${url}/${id}`);
  return response.data;
};

// 삽입
export const postEvent = async (event: Event) => {
  const response = await axios.post(`${url}/new`, event);
  return response.data;
};

// 삭제
export const deleteEvent = async (id: number) => {
  const response = await axios.delete(`${url}/${id}`);
  return response.data;
};

// 전체삭제
export const deleteEvents = async () => {
  const response = await axios.delete(`${url}/`);
  return response.data;
};
