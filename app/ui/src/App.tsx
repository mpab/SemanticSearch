import { BrowserRouter, Route, Switch } from "react-router-dom";
import "./App.css";
import { ManageSearchesView, SearchResultsView } from "./components/ApiViews";
import Footer from "./components/Footer";
import Home from "./components/Home";
import HowItWorks from "./components/HowItWorks";
import Navigation from "./components/Menu";
import Analysis from "./components/Analysis";

function App() {
  return (
    <>
      <BrowserRouter>
        <Navigation />

        <Switch>
          <Route path="/" exact component={Home}></Route>
          <Route path="/analysis" exact component={Analysis}></Route>
          <Route
            path="/search_results_view"
            exact
            component={SearchResultsView}
          ></Route>
          <Route
            path="/manage_searches_view"
            exact
            component={ManageSearchesView}
          ></Route>

          <Route path="/how_it_works" exact component={HowItWorks}></Route>
        </Switch>
        <Footer />
      </BrowserRouter>
    </>
  );
}

export default App;
