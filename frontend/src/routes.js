import Login from "./components/Login";
import Main from "./components/Main";
import Profile from "./components/Profile";
import Explore from "./components/Explore";
import Followings from "./components/Followings";
import UpcomingEvents from "./components/UpcomingEvents";
import EventHistory from "./components/EventHistory";
import EventTracker from "./components/EventTracker";
import CampusMap from "./components/CampusMap";
import LeaderBoard from "./components/LeaderBoard";
import ClubProfile from "./components/ClubProfile";
import OrganizeEvent from "./components/OrganizeEvent";
import EventResult from "./components/EventResult";
import RankBoardMember from "./components/RankBoardMember";
import AdvisorProfile from "./components/AdvisorProfile";

export const routes = [
  { path: "/", component: Login },
  { path: "/main", component: Main },
  { path: "/profile", component: Profile },
  { path: "/explore", component: Explore },
  { path: "/followings", component: Followings },
  { path: "/upcomingEvents", component: UpcomingEvents },
  { path: "/eventHistory", component: EventHistory },
  { path: "/eventTracker", component: EventTracker },
  { path: "/campusMap", component: CampusMap },
  { path: "/leaderboard", component: LeaderBoard },
  { path: "/clubProfile", component: ClubProfile },
  { path: "/organizeEvent", component: OrganizeEvent },
  { path: "/eventResult", component: EventResult },
  { path: "/rankBoardMember", component: RankBoardMember },
  { path: "/advisorProfile", component: AdvisorProfile }
];
