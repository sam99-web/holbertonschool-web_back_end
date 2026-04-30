export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  // CODE
  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this._code = value;
  }

  // NAME
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // METHOD
  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}

