import { useState } from "react";
import type { Event } from "../apis/eventApi";

type EventFormProps = {
  onSubmit: (event: Event) => void;
};

const EventForm = ({ onSubmit }: EventFormProps) => {
  // 폼 입력값 관리
  const [form, setForm] = useState<Event>({
    id: 1,
    title: "",
    image: "",
    description: "",
    tags: [],
    location: "",
  });

  const [tags, setTags] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    // setForm({
    //   ...form,
    //   [name]: value,
    // });
    setForm((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e: React.SubmitEvent) => {
    e.preventDefault();
    // tags : "python,fastapi,개발" => ['python','fastapi']
    const newEvent = {
      ...form,
      tags: tags.split(",").map((tag) => tag.trim()),
    };

    // 부모가 넘겨준 submit 함수 호출
    onSubmit(newEvent);

    // form 값 clear
    setForm({
      id: 1,
      title: "",
      image: "",
      description: "",
      tags: [],
      location: "",
    });
    // tags clear
    setTags("");
  };

  return (
    <form className="rounded-xl border bg-white p-6 shadow-sm" onSubmit={handleSubmit}>
      <h2 className="mb-6 text-xl font-bold">이벤트 등록</h2>

      <div className="space-y-4">
        {/* ID */}
        <div>
          <label className="mb-1 block text-sm font-medium">이벤트 ID</label>
          <input
            value={form.id}
            onChange={handleChange}
            type="number"
            name="id"
            className="w-full rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
        </div>

        {/* 제목 */}
        <div>
          <label className="mb-1 block text-sm font-medium">제목</label>
          <input
            value={form.title}
            onChange={handleChange}
            type="text"
            name="title"
            placeholder="이벤트 제목"
            required
            className="w-full rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
        </div>

        {/* 이미지 */}
        <div>
          <label className="mb-1 block text-sm font-medium">이미지 URL</label>
          <input
            value={form.image}
            onChange={handleChange}
            type="url"
            name="image"
            placeholder="https://..."
            required
            className="w-full rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
        </div>

        {/* 설명 */}
        <div>
          <label className="mb-1 block text-sm font-medium">설명</label>
          <textarea
            value={form.description}
            onChange={handleChange}
            name="description"
            placeholder="이벤트 설명"
            rows={4}
            required
            className="w-full resize-none rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
        </div>

        {/* 태그 */}
        <div>
          <label className="mb-1 block text-sm font-medium">태그</label>
          <input
            value={tags}
            onChange={(e) => setTags(e.target.value)}
            type="text"
            placeholder="python, fastapi, 개발"
            className="w-full rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
          <p className="mt-1 text-xs text-gray-400">쉼표(,)로 태그를 구분하세요.</p>
        </div>

        {/* 장소 */}
        <div>
          <label className="mb-1 block text-sm font-medium">장소</label>
          <input
            value={form.location}
            onChange={handleChange}
            type="text"
            name="location"
            placeholder="이벤트 장소"
            required
            className="w-full rounded-lg border px-4 py-2 outline-none focus:border-indigo-500"
          />
        </div>
        <button
          type="submit"
          className="w-full rounded-lg bg-indigo-600 py-3 font-semibold text-white hover:bg-indigo-700"
        >
          이벤트 등록
        </button>
      </div>
    </form>
  );
};

export default EventForm;
