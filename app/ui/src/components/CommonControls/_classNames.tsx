export class _classNames {
  static plainTitleText: string =
    " text-base text-left font-medium text-gray-900 ";

  static hoverTitleText: string =
    " text-base text-left font-medium text-gray-900 hover:text-app-medium ";

  static plainText: string = " text-left font-normal ";

  static hoverText: string = " text-left font-normal hover:text-app-medium ";

  static plainNode: string =
    _classNames.plainTitleText +
    " bg-white rounded-md inline-flex items-center focus:outline-none ";

  static hoverNode: string =
    _classNames.hoverTitleText +
    " bg-white rounded-md inline-flex items-center focus:outline-none ";

  static hoverLeaf: string =
    _classNames.hoverTitleText +
    " inline-flex items-center focus:outline-none ";

  static plainLeaf: string =
    _classNames.plainTitleText +
    " inline-flex items-center focus:outline-none ";

  static purpleBox: string =
    //_classNames.titleHoverText +
    " inline-flex items-center justify-center px-4 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-app-light border-app-dark border-t-2 border-l-2 border-r-2 border-b-4 hover:bg-app-medium ";
  static purpleHoverFrame: string =
    _classNames.hoverTitleText +
    " w-full rounded-md bg-gray-50 bg-opacity-50 px-4 py-2 flex items-start border-2 hover:border-app-light ";

  static invisibleFrameWithBorder: string =
    _classNames.plainTitleText +
    " w-full rounded-md px-4 py-2 flex items-start ";

  static invisibleFrame: string =
    _classNames.plainTitleText + " w-full rounded-md flex items-start ";

  static purplePlainFrame: string =
    _classNames.plainTitleText +
    " w-full rounded-md bg-gray-50 bg-opacity-50 px-4 py-2 flex items-start border-2 hover:border-app-light ";
  //" w-full rounded-md bg-gray-50 bg-opacity-50 px-4 py-2 flex items-start justify-between border-2 hover:border-app-light ";

  static headingText: string = " text-lg font-medium text-gray-900 ";
  static hoverInfoText: string = " mt-1 text-gray-900 hover:text-app-medium ";

  static hoverBackground: string =
    " -m-1 p-1 flex items-start rounded-lg block hover:bg-gray-50 ";

  static plainBackground: string =
    " -m-1 p-1 flex items-start rounded-lg block ";

  static image: string = " flex-shrink-0 w-5 ";
}
