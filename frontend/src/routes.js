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
import OemLogin from "./components/OemLogin";
import OemMain from "./components/OemMain";

const before = function(to, from, next) {
  if (localStorage.getItem("status") === "true") {
    next();
  } else {
    next("/");
  }
};

const beforeOem = function(to, from, next) {
  if (localStorage.getItem("OEMStatus") === "true") {
    next();
  } else {
    next("/");
  }
};

export const routes = [
  { name: "Login", path: "/", component: Login },
  {
    path: "/main",
    component: Main,
    beforeEnter: before
  },
  {
    name: "Profile",
    path: "/profile",
    beforeEnter: before,
    meta: { guest: false },
    component: Profile
  },
  {
    name: "Explore",
    path: "/explore",
    component: Explore,
    beforeEnter: before
  },
  { path: "/followings", component: Followings, beforeEnter: before },
  { path: "/upcomingEvents", component: UpcomingEvents, beforeEnter: before },
  { path: "/eventHistory", component: EventHistory, beforeEnter: before },
  { path: "/eventTracker", component: EventTracker, beforeEnter: before },
  { path: "/campusMap", component: CampusMap, beforeEnter: before },
  { path: "/leaderboard", component: LeaderBoard, beforeEnter: before },
  { path: "/clubProfile", component: ClubProfile, beforeEnter: before },
  { path: "/organizeEvent", component: OrganizeEvent, beforeEnter: before },
  { path: "/eventResult", component: EventResult, beforeEnter: before },
  { path: "/rankBoardMember", component: RankBoardMember, beforeEnter: before },
  { path: "/advisorProfile", component: AdvisorProfile, beforeEnter: before },
  { path: "/oemLogin", component: OemLogin },
  { path: "/oemMain", component: OemMain, beforeEnter: beforeOem }
];
