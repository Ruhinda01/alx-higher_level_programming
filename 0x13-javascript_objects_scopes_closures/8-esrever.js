#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length - 1;
  const arr = [];

  for (let i = size; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
