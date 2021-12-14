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
  { path: "/leaderboard", component: LeaderBoard }
];
