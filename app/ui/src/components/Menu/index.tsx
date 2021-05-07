import React from "react";
import { ReactElement } from "react";
import { Link } from "react-router-dom";
import { _classNames } from "../CommonControls/_classNames";

const Navigation = (): ReactElement => {
  const [isVisible, setIsVisible] = React.useState<boolean>(false);

  const onClick = () => {
    setIsVisible(!isVisible);
  };

  return (
    <div className="relative bg-white">
      <div className="border-b-2 border-gray-100">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 flex justify-between items-center py-6 md:justify-start md:space-x-10">
          <div className="flex justify-start lg:w-0 lg:flex-1">
            <img
              className="h-24 w-auto sm:h-10 float-left"
              src="./logo512.png"
              alt=""
            />
            <Link to="/" className="text-2xl text-gray-900 font-medium mx-3">
              Semantic Search Application
            </Link>
          </div>

          <div className="lg:hidden items-center justify-end md:flex-1 lg:w-0">
            <div className="-mr-2 -my-2 float-right">
              <button
                type="button"
                onClick={onClick}
                className="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500"
                aria-expanded="false"
              >
                <span className="sr-only">Open menu</span>
                <svg
                  className="h-6 w-6"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                </svg>
              </button>
            </div>
          </div>

          <nav className="hidden lg:flex space-x-7">
            <Link
              className={_classNames.hoverTitleText + " p-4"}
              to="/manage_searches_view"
            >
              Manage Searches
            </Link>

            <Link
              className={_classNames.hoverTitleText + " p-4"}
              to="/search_results_view"
            >
              Search Results
            </Link>

            <Link
              className={_classNames.hoverTitleText + " p-4"}
              to="/analysis"
            >
              Analysis
            </Link>

            <Link
              className={_classNames.hoverTitleText + " p-4"}
              to="/how_it_works"
            >
              How it works
            </Link>
          </nav>
        </div>
      </div>
    </div>
  );
};

export default Navigation;
