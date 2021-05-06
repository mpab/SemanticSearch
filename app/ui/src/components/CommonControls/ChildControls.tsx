import React, { ReactElement } from "react";
import { Link } from "react-router-dom";
import {
  LayoutImage,
  LayoutTitleWithHoverSubtitles,
  LayoutTitleWithPlainSubtitles,
  LayoutTitleWithValue,
} from "./Elements";
import { ControlProps } from "./Models";
import { _classNames } from "./_classNames";

export const LeafLabel: React.FC<ControlProps> = (props): ReactElement => {
  return (
    <div key={props.itemKey} className={_classNames.plainBackground}>
      <LayoutImage {...props} />
      <LayoutTitleWithValue {...props} />
    </div>
  );
};

export const LeafLabelList: React.FC<ControlProps> = (props): ReactElement => {
  return (
    <div key={props.itemKey} className={_classNames.plainBackground}>
      <label className={props.className}>
        <LayoutImage {...props} />
        <LayoutTitleWithPlainSubtitles {...props} />
      </label>
    </div>
  );
};

export const LeafButton: React.FC<ControlProps> = (props): ReactElement => {
  if (!props.getIsVisible()) return <></>;

  return (
    <div key={props.itemKey} className={_classNames.hoverBackground}>
      <button onClick={props.onClick} className={props.className}>
        <LayoutImage {...props} />
        <LayoutTitleWithHoverSubtitles {...props} />
      </button>
    </div>
  );
};

export const LeafSelect: React.FC<ControlProps> = (props): ReactElement => {
  const [values, setValues] = React.useState(
    props.getValues ? props.getValues() : []
  );
  const [value, setValue] = React.useState(
    props.getValue ? props.getValue() : ""
  );

  const onSelect = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setValue(e.target.value);
    if (props.onSelect) {
      props.onSelect(e);
    }
  };

  React.useEffect(() => {
    setValues(props.getValues ? props.getValues() : []);
  }, [props]);

  React.useEffect(() => {
    setValue(props.getValue ? props.getValue() : "");
  }, [props]);

  if (!props.getIsVisible()) return <></>;

  return (
    <div key={props.itemKey} className={_classNames.plainBackground}>
      <label className={_classNames.invisibleFrameWithBorder}>
        {props.title}
      </label>
      <select className={props.className} onChange={onSelect} value={value}>
        {values.map((item) => (
          <option key={item} value={item}>
            {item}
          </option>
        ))}
      </select>
    </div>
  );
};

export const LeafInput: React.FC<ControlProps> = (props): ReactElement => {
  const [value, setValue] = React.useState(
    props.getValue ? props.getValue() : ""
  );

  React.useEffect(() => {
    setValue(props.getValue ? props.getValue() : "");
  }, [props]);

  const onSubmit = (): void => {
    if (value && props.onSubmit) {
      props.onSubmit(value);
    }
  };

  const onKeyDown = (event: React.KeyboardEvent<HTMLDivElement>): void => {
    // 'keypress' event misbehaves on mobile so we track 'Enter' key via 'keydown' event
    if (event.key === "Enter") {
      event.preventDefault();
      event.stopPropagation();
      onSubmit();
    }
  };

  const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (props.onChange) {
      props.onChange(e);
    }
    setValue(e.target.value);
  };

  if (!props.getIsVisible()) return <></>;

  return (
    <div key={props.itemKey} className={_classNames.plainBackground}>
      <label className={_classNames.invisibleFrameWithBorder}>
        {props.title}
      </label>
      <input
        readOnly={props.getIsReadOnly()}
        className={props.className}
        type={props.inputType}
        value={value}
        onChange={onChange}
        onKeyDown={onKeyDown}
      />
    </div>
  );
};

export const LeafUrl: React.FC<ControlProps> = (props): ReactElement => {
  if (!props.getIsVisible()) return <></>;

  return (
    <div key={props.itemKey} className="flex items-start">
      {props.link ? (
        <a
          target="_blank"
          rel="noopener noreferrer"
          href={props.link}
          className={props.className}
        >
          <LayoutImage {...props} />
          <LayoutTitleWithHoverSubtitles {...props} />
        </a>
      ) : (
        <></>
      )}
    </div>
  );
};

export const LeafLink: React.FC<ControlProps> = (props): ReactElement => {
  if (!props.getIsVisible()) return <></>;

  return (
    <div key={props.itemKey} className="flex items-start">
      <div className={props.className}>
        <LayoutImage {...props} />
        <Link to={props.link ? props.link : ""}>
          <LayoutTitleWithHoverSubtitles {...props} />
        </Link>
      </div>
    </div>
  );
};
