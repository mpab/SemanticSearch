export class StringUtil {
  static arrayToString = (array: string[], sep: string = ", "): string => {
    let result = "";
    for (let i = 0; i !== array.length; ++i) {
      if (i === 0) {
        result = array[i];
      } else {
        result = result + sep + array[i];
      }
    }
    return result;
  };

  static stringToArray = (str: string, sep: string = ", "): string[] => {
    return str.split(sep);
  };
}
