import type { Event } from "../apis/eventApi";

type EventCardProps = {
  event: Event;
  onDelete: (id: number) => void;
};
const EventCard = ({ event, onDelete }: EventCardProps) => {
  return (
    <div className="overflow-hidden rounded-xl border bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-md">
      {/* 이미지 */}
      <img src={event.image} alt={event.title} className="h-48 w-full object-cover" />

      <div className="p-5">
        {/* 제목 */}
        <h2 className="mb-2 text-xl font-bold text-gray-900">{event.title}</h2>

        {/* 설명 */}
        <p className="mb-4 line-clamp-2 text-sm text-gray-600">{event.description}</p>

        {/* 위치 */}
        <div className="mb-4 flex items-center gap-2 text-sm text-gray-500">
          <span>📍</span>
          <span>{event.location}</span>
        </div>

        {/* 태그 */}
        <div className="mb-5 flex flex-wrap gap-2">
          {event.tags.map((tag) => (
            <span key={tag} className="rounded-full bg-indigo-50 px-3 py-1 text-xs font-medium text-indigo-600">
              {tag}
            </span>
          ))}
        </div>

        {/* 삭제 버튼 */}
        <button
          onClick={() => onDelete(event.id)}
          className="w-full rounded-lg border border-red-200 py-2 text-sm font-medium text-red-500 transition hover:bg-red-50"
        >
          삭제
        </button>
      </div>
    </div>
  );
};

export default EventCard;
