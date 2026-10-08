import { Link, NavLink } from "react-router-dom";

const Header = () => {
    return (
        <header className="sticky top-0 z-50 border-b border-gray-200 bg-white/95 backdrop-blur">
            <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">

                {/* 로고 */}
                <Link
                    to="/"
                    className="flex items-center gap-2"
                >
                    <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-600 text-lg font-bold text-white">
                        E
                    </div>

                    <span className="text-xl font-bold text-gray-900">
                        Event Planner
                    </span>
                </Link>

                {/* 중앙 메뉴 */}
                <nav className="hidden items-center gap-8 md:flex">

                    <NavLink
                        to="/events"
                        className={({ isActive }) =>
                            `text-sm font-medium transition ${isActive
                                ? "text-indigo-600"
                                : "text-gray-600 hover:text-indigo-600"
                            }`
                        }
                    >
                        이벤트
                    </NavLink>




                </nav>

                {/* 오른쪽 메뉴 */}
                <div className="flex items-center gap-3">

                    <Link
                        to="/login"
                        className="hidden px-3 py-2 text-sm font-medium text-gray-600 hover:text-indigo-600 sm:block"
                    >
                        로그인
                    </Link>

                    <Link
                        to="/signup"
                        className="rounded-lg bg-indigo-600 px-4 py-2 text-sm font-semibold text-white transition hover:bg-indigo-700"
                    >
                        회원가입
                    </Link>

                </div>

            </div>
        </header>
    );
};

export default Header;

