import { Transition } from "@windmill/react-ui";
import React, { ReactElement } from "react";
import { LayoutImage, LayoutTitleWithHoverSubtitles } from "./Elements";
import {
  LeafButton,
  LeafLink,
  LeafSelect,
  LeafUrl,
  LeafInput,
  LeafLabel,
  LeafLabelList,
} from "./ChildControls";
import { ControlType, ControlProps, ChildPolicy } from "./Models";
import { ModalDialog } from "./ModalDialog";

export const Control: React.FC<ControlProps> = (
  props: ControlProps
): ReactElement => {
  switch (props.controlType) {
    // case ControlType.NodeForm:
    //   return <NodeForm {...props} />;

    case ControlType.ModalDialogPopupButton:
      return <ModalDialogPopupButton {...props} />;

    case ControlType.HoverPopupLabel:
      return <HoverPopupLabel {...props} />;

    case ControlType.Button:
      return <LeafButton {...props} />;

    case ControlType.Link:
      return <LeafLink {...props} />;

    case ControlType.Label:
      return <LeafLabel {...props} />;

    case ControlType.LabelList:
      return <LeafLabelList {...props} />;

    case ControlType.Url:
      return <LeafUrl {...props} />;

    case ControlType.Input:
      return <LeafInput {...props} />;

    case ControlType.Select:
      return <LeafSelect {...props} />;

    default:
      return <></>;
  }
};

const ParentControl: React.FC<ControlProps> = (
  props: ControlProps
): ReactElement => {
  const container = props;
  const type = props.controlType;
  const areNodesVisible = props.areChildrenVisible;

  return (
    <div className="-m-1 p-1 flex items-start">
      <button
        type="button"
        onClick={props.onClick}
        className={container.className}
        aria-expanded="false"
      >
        <LayoutImage {...props} />
        <LayoutTitleWithHoverSubtitles {...props} />

        {type === ControlType.HoverPopupLabel && areNodesVisible ? (
          <svg
            className="ml-2 h-5 w-5 group-hover:text-app-medium"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fillRule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clipRule="evenodd"
            />
          </svg>
        ) : (
          <></>
        )}

        {type === ControlType.HoverPopupLabel && !areNodesVisible ? (
          <svg
            className={
              container.children // further information is available
                ? "ml-2 w-5 h-5 hover:text-app-dark animate-pulse"
                : "ml-2 w-5 h-5 hover:text-app-dark"
            }
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fillRule="evenodd"
              d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
              clipRule="evenodd"
            />
          </svg>
        ) : (
          <></>
        )}
      </button>
    </div>
  );
};

interface OmniProps {
  item: ControlProps;
  itemKey?: number;
  areChildrenVisible?: boolean;
  parentClassName?: string;
  onClick?: React.MouseEventHandler<HTMLButtonElement>;
}

const OmniChild: React.FC<OmniProps> = ({
  item,
  itemKey,
  areChildrenVisible,
  parentClassName,
  onClick,
}: OmniProps): ReactElement => {
  const newItem = Object.assign({}, item); //copy object
  newItem.itemKey = itemKey;
  newItem.areChildrenVisible = areChildrenVisible;
  newItem.parentClassName = parentClassName;
  newItem.onClick = onClick ? onClick : item.onClick;
  return <Control {...newItem}></Control>;
};

const OmniParent: React.FC<OmniProps> = ({
  item,
  itemKey,
  areChildrenVisible,
  parentClassName,
  onClick,
}: OmniProps): ReactElement => {
  const newItem = Object.assign({}, item); //copy object
  newItem.itemKey = itemKey;
  newItem.areChildrenVisible = areChildrenVisible;
  newItem.parentClassName = parentClassName;
  newItem.onClick = onClick ? onClick : item.onClick;
  return <ParentControl {...newItem}></ParentControl>;
};

export const HoverPopupLabel: React.FC<ControlProps> = (
  props
): ReactElement => {
  const [isVisible, setIsVisible] = React.useState<boolean>(false);

  const handleOnMouseEnterLeave = () => {
    setIsVisible(!isVisible);
    if (props.onToggleVisible) {
      props.onToggleVisible(!isVisible);
    }
  };

  return (
    <div
      className={props.parentClassName}
      onMouseEnter={handleOnMouseEnterLeave}
      onMouseLeave={handleOnMouseEnterLeave}
    >
      <OmniParent item={props} areChildrenVisible={isVisible}></OmniParent>

      <Transition
        show={isVisible}
        enter="transition ease-out duration-200"
        enterFrom="opacity-0 translate-y-1"
        enterTo="opacity-100 translate-y-0"
        leave="transition ease-in duration-150"
        leaveFrom="opacity-100 translate-y-0"
        leaveTo="opacity-0 translate-y-1"
      >
        <div className="absolute z-10 -ml-4 pt-3 transform px-2 w-screen max-w-sm sm:px-0 lg:ml-0 lg:left-1/2 lg:-translate-x-1/2">
          <div className="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 overflow-hidden">
            <div className="relative grid gap-8 bg-white sm:gap-4 sm:p-4">
              {props.header ? (
                <h3 className="text-lg leading-6 font-medium text-gray-900">
                  {props.header}
                </h3>
              ) : (
                <></>
              )}
              {props.children?.map((item, index) => {
                return (
                  <OmniChild
                    item={item}
                    key={index}
                    parentClassName={props.parentClassName}
                  />
                );
              })}
              {props.footer ? <span>{props.footer}</span> : <></>}
            </div>
          </div>
        </div>
      </Transition>
    </div>
  );
};

const ModalDialogPopupButton: React.FC<ControlProps> = (
  props: ControlProps
): ReactElement => {
  const [isVisible, setVisible] = React.useState(false);
  const toggleModalPopup = () => {
    setVisible(!isVisible);
    if (props.onToggleVisible) {
      props.onToggleVisible(!isVisible);
    }
  };

  const handleOnClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    // console.log("ModalDialogPopupButton: handleOnClick");
    toggleModalPopup();
  };

  const handleChildOnClick = (
    event: React.MouseEvent<HTMLButtonElement>,
    item: ControlProps
  ): void => {
    // console.log("ModalDialogPopupButton: handleChildOnClick");
    // console.log(
    //   item.onClick
    //     ? "- handleChildOnClick has handler"
    //     : "- handleChildOnClick no handler"
    // );
    // console.log("- handleChildOnClick policy: " + props.policy);

    if (item.onClick) item.onClick(event);
    if (props.policy && props.policy === ChildPolicy.CloseIfAnyClicked)
      toggleModalPopup();
  };

  return (
    <div className={props.parentClassName}>
      <OmniParent
        item={props}
        areChildrenVisible={isVisible}
        onClick={(event) => {
          handleOnClick(event);
        }}
      ></OmniParent>

      <ModalDialog
        isOpen={isVisible}
        onClose={toggleModalPopup}
        title={props.header}
      >
        {props.children?.map((item, index) => {
          return (
            <OmniChild
              item={item}
              itemKey={index}
              parentClassName={props.parentClassName}
              onClick={(event) => {
                handleChildOnClick(event, item);
              }}
            />
          );
        })}

        {props.footer ? <span>{props.footer}</span> : <></>}
      </ModalDialog>
    </div>
  );
};

// export const NodeForm: React.FC<ControlProps> = (
//   props: ControlProps
// ): ReactElement => {
//   const [isVisible, setVisible] = React.useState(false);
//   const toggleModalPopup = () => {
//     // console.log("NodeModalButton:toggleModalPopup");
//     setVisible(!isVisible);
//   };

//   const handleOnClick = (event: React.MouseEvent<HTMLButtonElement>) => {
//     toggleModalPopup();
//   };

//   return (
//     <div className={props.nodeClassName}>
//       <NodeControl
//         controlType={props.controlType}
//         inputType={props.inputType}
//         title={props.title}
//         image={props.image}
//         onClick={(event) => {
//           handleOnClick(event);
//         }}
//         link={props.link}
//         subtitles={props.subtitles}
//         subtitlesIndex={props.subtitlesIndex}
//         className={props.className}
//         areNodesVisible={isVisible}
//         nodes={props.nodes}
//         header={props.header}
//         footer={props.footer}
//       ></NodeControl>

//       <NodeModal
//         isOpen={isVisible}
//         onClose={toggleModalPopup}
//         title={props.header}
//       >
//         <form>
//           {props.nodes?.map((item, index) => {
//             return (
//               <OmniItem
//                 item={item}
//                 key={index}
//                 nodeClassName={props.nodeClassName}
//               />
//             );
//           })}
//         </form>
//         {props.footer ? <span>{props.footer}</span> : <></>}
//       </NodeModal>
//     </div>
//   );
// };
