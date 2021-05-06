import { AppearanceTypes } from "react-toast-notifications";

// for use by toasts

import { ReactNode } from "react";

export enum BreadType {
  Info,
  Success,
  Warning,
  Fail,
  Exception, //FATAL
}

export declare interface BreadProperties {
  messages: string[];
  type: BreadType;
}

export const InfoBread = (
  title: string,
  messages: string[]
): BreadProperties => {
  return {
    messages: messages,
    type: BreadType.Info,
  };
};

export const SuccessBread = (messages: string[]): BreadProperties => {
  return {
    messages: messages,
    type: BreadType.Success,
  };
};

export const WarningBread = (messages: string[]): BreadProperties => {
  return {
    messages: messages,
    type: BreadType.Warning,
  };
};

export const FailBread = (messages: string[]): BreadProperties => {
  return {
    messages: messages,
    type: BreadType.Fail,
  };
};

export const ExceptionBread = (messages: string[]): BreadProperties => {
  return {
    messages: messages,
    type: BreadType.Exception,
  };
};

declare interface Params {
  content: ReactNode;
  appearance: AppearanceTypes;
  autoDismiss: boolean;
}

export const BreadConvert = (props: BreadProperties): Params => {
  let content = "";
  for (const idx in props.messages) {
    if (idx === "0") {
      content = props.messages[idx];
    } else if (idx === "1") {
      content = content + ": " + props.messages[idx];
    } else {
      content = content + ", " + props.messages[idx];
    }
  }

  switch (props.type) {
    case BreadType.Info:
      return {
        content: content,
        appearance: "success",
        autoDismiss: true,
      };

    case BreadType.Success:
      return {
        content: content,
        appearance: "success",
        autoDismiss: true,
      };

    case BreadType.Warning:
      return {
        content: content,
        appearance: "warning",
        autoDismiss: true,
      };

    case BreadType.Fail:
    case BreadType.Exception:
    default:
      return {
        content: content,
        appearance: "error",
        autoDismiss: false,
      };
  }
};
