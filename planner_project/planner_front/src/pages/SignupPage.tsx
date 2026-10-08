import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { postNewUser } from "../apis/userApi";

const SignupPage = () => {
  const [form, setForm] = useState({ email: "", password: "", passwordCheck: "" });
  const { email, password, passwordCheck } = form;
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
    // 비밀번호 일치 여부
    if (password !== passwordCheck) {
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }
    try {
      await postNewUser(email, password);
      navigate("/login");
    } catch (error) {}
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-sm">
        <h1 className="mb-2 text-2xl font-bold">회원가입</h1>

        <p className="mb-8 text-sm text-gray-500">Event Planner 계정을 만들어보세요.</p>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="mb-1 block text-sm font-medium">이메일</label>

            <input
              name="email"
              value={email}
              onChange={handleChange}
              type="email"
              required
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
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium">비밀번호 확인</label>
            <input
              type="password"
              name="passwordCheck"
              value={passwordCheck}
              onChange={handleChange}
              required
              className="w-full rounded-lg border px-4 py-3 outline-none focus:border-indigo-500"
            />
          </div>

          <button
            type="submit"
            className="w-full rounded-lg bg-indigo-600 py-3 font-semibold text-white hover:bg-indigo-700"
          >
            회원가입
          </button>
        </form>

        <p className="mt-6 text-center text-sm text-gray-500">
          이미 계정이 있으신가요?
          <Link to="/login" className="font-medium text-indigo-600 hover:underline">
            로그인
          </Link>
        </p>
      </div>
    </div>
  );
};

export default SignupPage;
