import React, { ReactElement } from "react";
import { useToasts } from "react-toast-notifications";
import {
  ButtonProps,
  ChildPolicy,
  ModalDialogPopupButtonProps,
} from "./CommonControls/Models";
import { Control } from "./CommonControls/ParentControls";
import { _classNames } from "./CommonControls/_classNames";

import { BreadConvert, SuccessBread } from "./Toast";

export const ModalDialogPopupButton = (): ReactElement => {
  const props = ModalDialogPopupButtonProps({
    header: "Test Dialog",
    footer: "",
    title: "Dialog Test",
    image: "",
    policy: ChildPolicy.NeverCloseIfAnyClicked,
    children: [],
    className: _classNames.purplePlainFrame,
  });

  return <Control {...props} />;
};

export const ToastButton = (): ReactElement => {
  const { addToast } = useToasts();

  const onClick = async () => {
    const p = BreadConvert(SuccessBread(["Success!"]));
    addToast(p.content, {
      appearance: p.appearance,
      autoDismiss: p.autoDismiss,
    });
  };

  const props = ButtonProps({
    title: "Toast Test",
    image: "",
    onClick: onClick,
    className: _classNames.purplePlainFrame,
  });

  return <Control {...props} />;
};
