import React, { ReactElement } from "react";
import { Transition } from "@windmill/react-ui";
import { PortalContext } from "./PortalContext";
interface ModalProps {
  title: string;
  isOpen: boolean;
  onClose: () => void;
}

// Archangel: renamed to discriminate between this Modal and the Modal defined in @windmill/react-ui
export const ModalDialog: React.FC<ModalProps> = ({
  title,
  isOpen,
  onClose,
  children,
}): ReactElement => {
  const overlayRef = React.useRef(null);
  const handleOverlayClick = (e: React.MouseEvent<HTMLElement, MouseEvent>) => {
    // close when clicking outside
    if (e.target === overlayRef.current) {
      onClose();
    }
  };

  // Archangel: IMPORTANT NOTE
  // PortalContext is the magic that injects this JSX
  // fragment into the DOM at the root level
  return isOpen ? (
    <PortalContext>
      <div
        className="fixed z-10 inset-0 overflow-y-auto"
        aria-labelledby="modal-title"
        role="dialog"
        aria-modal="true"
      >
        <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
          <div
            className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
            aria-hidden="true"
            ref={overlayRef}
            onClick={handleOverlayClick}
          ></div>

          <span
            className="hidden sm:inline-block sm:align-middle sm:h-screen"
            aria-hidden="true"
          >
            &#8203;
          </span>
          <Transition
            show={isOpen}
            enter="transition ease-out duration-100 transform"
            enterFrom="opacity-0 scale-95"
            enterTo="opacity-100 scale-100"
            leave="transition ease-in duration-75 transform"
            leaveFrom="opacity-100 scale-100"
            leaveTo="opacity-0 scale-95"
          >
            <div className="inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-sm sm:w-full sm:p-6">
              <div className="hidden sm:block absolute top-0 right-0 pt-4 pr-4">
                <button
                  type="button"
                  onClick={onClose}
                  className="bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-app-light"
                >
                  <span className="sr-only">Close</span>
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
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                </button>
              </div>

              <div className="px-4 py-5 grid gap-4 sm:gap-4 sm:p-0">
                <h3 className="text-lg leading-6 font-medium text-gray-900 mb-2">
                  {title}
                </h3>

                {children}
              </div>
            </div>
          </Transition>
        </div>
      </div>
    </PortalContext>
  ) : (
    <></>
  );
};
