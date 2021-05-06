import { _classNames } from "./_classNames";

export const ControlType = {
  //NodeForm: "NodeForm",
  ModalDialogPopupButton: "ModalDialogPopupButton",
  HoverPopupLabel: "HoverPopupLabel",

  Button: "LeafButton",
  Link: "LeafLink",
  Url: "LeafUrl",
  Label: "LeafLabel",
  LabelList: "LeafLabelList",
  Input: "LeafInput",
  Select: "LeafSelect",
} as const;
// eslint-disable-next-line @typescript-eslint/no-redeclare
export type ControlType = typeof ControlType[keyof typeof ControlType];

export const InputType = {
  Text: "text",
  Number: "number",
  Url: "url",
  Email: "email",
} as const;
// eslint-disable-next-line @typescript-eslint/no-redeclare
export type InputType = typeof InputType[keyof typeof InputType];

export const ChildPolicy = {
  NeverCloseIfAnyClicked: "NeverCloseIfAnyClicked", // must use the close button, default
  CloseIfAnyClicked: "CloseIfAnyClicked", // any action closes
} as const;
// eslint-disable-next-line @typescript-eslint/no-redeclare
export type NodesPolicy = typeof ChildPolicy[keyof typeof ChildPolicy];

type OnSelectFn = (e: React.ChangeEvent<HTMLSelectElement>) => void;
type OnChangeFn = (e: React.ChangeEvent<HTMLInputElement>) => void;
type OnSubmitFn = (value: string) => void;
type OnToggleVisibleFn = (isVisible: boolean) => void;
type GetValueFn = () => string;
type GetValuesFn = () => string[];
type GetBooleanPropertyFn = () => boolean;

// TODO: merge and make consistent all the way down
// props->props->props
export declare interface ControlProps {
  // common properties
  controlType: ControlType;
  className: string;
  title?: string;
  image?: string;
  link?: string;
  subtitles: string[];
  inputType?: InputType; // text, number, ...

  onClick?: React.MouseEventHandler<HTMLButtonElement>;
  onSelect?: OnSelectFn;
  onChange?: OnChangeFn;
  onSubmit?: OnSubmitFn;
  getValue?: GetValueFn;
  getValues?: GetValuesFn;
  onToggleVisible?: OnToggleVisibleFn; // the control calls this when its visible state changes
  getIsVisible: GetBooleanPropertyFn; // the control reads this to determine if is should show/hide itself
  getIsReadOnly: GetBooleanPropertyFn; // false for e.g. readonly props...

  itemKey?: number; // Archangel: hack for now

  // the following are if this node has child nodes
  children?: ControlProps[];
  header: string;
  footer: string;
  parentClassName?: string;
  areChildrenVisible?: boolean;
  policy?: NodesPolicy;
}

// interface nodeFormParams {
//   title: string;
//   image: string;
//   header: string;
//   footer: string;
//   policy: NodesPolicy;
//   nodes: ControlProps[];
//   nodeClassName?: string;
//   className?: string;
//   //subTitles?: string[];
// }

// export const NodeFormProps = (params: nodeFormParams): ControlProps => ({
//   controlType: ControlType.NodeForm,
//   title: params.title,
//   image: params.image,
//   header: params.header,
//   footer: params.footer,
//   policy: params.policy,
//   nodes: params.nodes,
//   nodeClassName: params.nodeClassName,
//   className: params.className ? params.className : _classNames.hoverNode,
//   subtitles: [],
//   subtitlesIndex: -1,
// });

interface modalDialogPopupButtonParams {
  title: string;
  image: string;
  header: string;
  footer: string;
  policy: NodesPolicy;
  children: ControlProps[];
  parentClassName?: string;
  className?: string;
  subtitles?: string[];
  onToggleVisible?: OnToggleVisibleFn;
  getIsVisible?: GetBooleanPropertyFn;
}

export const ModalDialogPopupButtonProps = (
  params: modalDialogPopupButtonParams
): ControlProps => ({
  controlType: ControlType.ModalDialogPopupButton,
  title: params.title,
  image: params.image,
  header: params.header,
  footer: params.footer,
  policy: params.policy,
  children: params.children,
  className: params.className ? params.className : _classNames.hoverNode,
  subtitles: params.subtitles ?? [],
  onToggleVisible: params.onToggleVisible
    ? params.onToggleVisible
    : (isVisible: boolean) => {},
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

interface hoverPopupLabelParams {
  title: string;
  image: string;
  header: string;
  footer: string;
  children: ControlProps[];
  nodeClassName?: string;
  className?: string;
  getIsVisible?: GetBooleanPropertyFn;
}

export const HoverPopupLabelProps = (
  params: hoverPopupLabelParams
): ControlProps => ({
  controlType: ControlType.HoverPopupLabel,
  title: params.title,
  image: params.image,
  header: params.header,
  footer: params.footer,
  policy: ChildPolicy.NeverCloseIfAnyClicked,
  children: params.children,
  parentClassName: params.nodeClassName,
  className: params.className ?? _classNames.hoverNode,
  subtitles: [],
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

interface ButtonParams {
  title: string;
  image: string;
  onClick: React.MouseEventHandler<HTMLButtonElement>;
  className?: string;
  subtitles?: string[];
  getIsVisible?: GetBooleanPropertyFn;
}

export const ButtonProps = (params: ButtonParams): ControlProps => ({
  controlType: ControlType.Button,
  title: params.title,
  image: params.image,
  onClick: params.onClick,
  className: params.className ?? _classNames.hoverLeaf,
  subtitles: params.subtitles ?? [],
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

interface linkParams {
  title: string;
  image: string;
  link: string;
  subtitles: string[];
  className?: string;
  getIsVisible?: GetBooleanPropertyFn;
}

export const LinkProps = (params: linkParams): ControlProps => ({
  controlType: ControlType.Link,
  title: params.title,
  image: params.image,
  link: params.link,
  className: params.className ?? _classNames.hoverLeaf,
  subtitles: params.subtitles ?? [],
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

export const UrlProps = (params: linkParams): ControlProps => ({
  controlType: ControlType.Url,
  title: params.title,
  image: params.image,
  link: params.link,
  className: params.className ?? _classNames.hoverLeaf,
  subtitles: [],
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

export declare interface LabelInputParams {
  title: string;
  image?: string;
  inputType?: InputType;
  className?: string;
  onChange?: OnChangeFn;
  onSubmit?: OnSubmitFn;
  getValue?: GetValueFn;
  getIsVisible?: GetBooleanPropertyFn;
  getIsReadOnly?: GetBooleanPropertyFn;
}

export const LabelProps = (params: LabelInputParams): ControlProps => ({
  controlType: ControlType.Label,
  title: params.title,
  image: params.image,
  inputType: params.inputType ?? InputType.Text,
  getValue: params.getValue,
  className: params.className ?? _classNames.invisibleFrameWithBorder,
  subtitles: [],
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: params.getIsReadOnly
    ? params.getIsReadOnly
    : () => {
        return false;
      },
});

export const InputProps = (params: LabelInputParams): ControlProps => ({
  controlType: ControlType.Input,
  title: params.title,
  inputType: params.inputType ?? InputType.Text,
  getValue: params.getValue,
  className: params.className ?? _classNames.invisibleFrameWithBorder,
  subtitles: [],
  onChange: params.onChange,
  onSubmit: params.onSubmit,
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: params.getIsReadOnly
    ? params.getIsReadOnly
    : () => {
        return false;
      },
});

export declare interface LabelListParams {
  title: string;
  image?: string;
  inputType?: InputType;
  className?: string;
  subtitles?: string[];
  subTitlesIndex?: number;
  getIsVisible?: GetBooleanPropertyFn;
}

export const LabelListProps = (params: LabelListParams): ControlProps => ({
  controlType: ControlType.LabelList,
  title: params.title,
  image: params.image,
  inputType: params.inputType ?? InputType.Text,
  className: params.className ?? _classNames.invisibleFrame,
  subtitles: params.subtitles ?? [],
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});

interface textSelectParams {
  title: string;
  image: string;
  className?: string;
  onSelect: OnSelectFn;
  getValue: GetValueFn;
  getValues: GetValuesFn;
  getIsVisible?: GetBooleanPropertyFn;
}

export const TextSelectProps = (params: textSelectParams): ControlProps => ({
  controlType: ControlType.Select,
  title: params.title,
  subtitles: [],
  image: params.image,
  className: params.className ?? _classNames.invisibleFrameWithBorder,
  onSelect: params.onSelect,
  getValue: params.getValue,
  getValues: params.getValues,
  header: "",
  footer: "",
  getIsVisible: params.getIsVisible
    ? params.getIsVisible
    : () => {
        return true;
      },
  getIsReadOnly: () => {
    return true;
  },
});
