import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";
import { signin } from "../apis/userApi";

const LoginPage = () => {
  const [form, setForm] = useState({ email: "", password: "" });
  const { email, password } = form;

  const navigate = useNavigate();

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.SubmitEvent) => {
    e.preventDefault();

    try {
      signin(email, password);
      // 페이지 이동 /events
      navigate("/events");
    } catch (error: any) {
      const message = error.response?.data?.detail ?? "로그인에 실패했습니다.";
      alert(message);
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-sm">
        <h1 className="mb-2 text-2xl font-bold">로그인</h1>

        <p className="mb-8 text-sm text-gray-500">Event Planner에 로그인하세요.</p>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="mb-1 block text-sm font-medium">이메일</label>

            <input
              name="email"
              value={email}
              onChange={handleChange}
              type="email"
              required
              placeholder="example@email.com"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium">비밀번호</label>
            <input
              name="password"
              value={password}
              onChange={handleChange}
              type="password"
              required
              placeholder="비밀번호"
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-indigo-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-lg bg-indigo-600 py-3 font-semibold text-white hover:bg-indigo-700"
          >
            로그인
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-gray-500">
          계정이 없으신가요?{" "}
          <Link to="/signup" className="font-medium text-indigo-600 hover:underline">
            회원가입
          </Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
