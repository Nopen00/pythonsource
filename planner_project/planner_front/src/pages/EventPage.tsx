import { useEffect, useState } from "react";
import { deleteEvent, getEvents, postEvent, type Event } from "../apis/eventApi";
import EventCard from "../components/EventCard";
import EventForm from "../components/EventForm";

const EventPage = () => {
  const [events, setEvents] = useState<Event[]>([]);
  const [loading, setLoading] = useState(false);

  // 이벤트 조회
  const fetchEvents = async () => {
    try {
      setLoading(true);
      const data = await getEvents();
      setEvents(data);
    } catch (error) {
      console.log(error);
    } finally {
      setLoading(false);
    }
  };

  // 최초 렌더링
  useEffect(() => {
    fetchEvents();
  }, []);

  // 이벤트 등록
  const handleCreate = async (event: Event) => {
    try {
      await postEvent(event);
      await fetchEvents();
    } catch (error) {
      console.log(error);
    }
  };

  // 이벤트 삭제
  const handleDelete = async (id: number | undefined) => {
    if (!id) return;

    const confirmed = confirm("정말 삭제하시겠습니까?");
    if (!confirmed) return;

    try {
      await deleteEvent(id);
      await fetchEvents();
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="border-b bg-white">
        <div className="mx-auto max-w-6xl px-6 py-8">
          <h1 className="text-3xl font-bold text-gray-900">Event Planner</h1>

          <p className="mt-2 text-gray-500">나만의 이벤트를 관리해보세요.</p>
        </div>
      </div>

      <main className="mx-auto max-w-6xl px-6 py-10">
        {/* 등록 */}
        <section className="mb-12">
          <EventForm onSubmit={handleCreate} />
        </section>

        {/* 이벤트 목록 */}
        <section>
          <div className="mb-6 flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold">이벤트 목록</h2>

              <p className="mt-1 text-sm text-gray-500">총 {events.length} 개의 이벤트</p>
            </div>

            <button className="rounded-lg border bg-white px-4 py-2 text-sm hover:bg-gray-50">새로고침</button>
          </div>
          {loading ? (
            <div className="py-20 text-center text-gray-500">이벤트를 불러오는 중...</div>
          ) : events.length === 0 ? (
            <div className="rounded-xl border bg-white py-20 text-center">
              <p className="text-gray-500">등록된 이벤트가 없습니다.</p>
            </div>
          ) : (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {events.map((event) => (
                <EventCard key={event.id} event={event} onDelete={handleDelete} />
              ))}
            </div>
          )}
        </section>
      </main>
    </div>
  );
};

export default EventPage;
