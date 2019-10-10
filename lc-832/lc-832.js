/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function (A) {
  const invertedGrid = [];

  for (let i = 0; i < A.length; i += 1) {
    const row = []
    for (let j = A[i].length - 1; j >= 0; j -= 1) {
      const ele = A[i][j] === 0 ? 1 : 0;
      row.push(ele);
    }

    invertedGrid.push(row);
  }

  return invertedGrid;
};