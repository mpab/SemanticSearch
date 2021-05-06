import * as React from "react";
import * as ReactDOM from "react-dom";

export type ModalProps = {
  children: any;
};
export type ModalState = any;

export const PortalContext: React.FC = (
  props
): React.ReactElement<ModalProps, ModalState> => {
  const modalRoot = React.useRef<HTMLElement>(
    document.getElementById("root-modal") || document.createElement("div")
  ).current;
  const container = React.useRef<HTMLDivElement>(document.createElement("div"))
    .current;

  React.useEffect(() => {
    //console.log("componentDidMount()");
    modalRoot.className = "root-modal";
    modalRoot.appendChild(container); // insert into DOM

    return () => {
      //console.log("componentWillUnmount()");
      modalRoot.removeChild(container); // remove from DOM
    };
  }, [container, modalRoot]);

  //console.log("PortalContext: render()");
  return ReactDOM.createPortal(props.children, container);
};
