var generate = function (numRows) {
  if (numRows === 0) return [];
  if (numRows === 1) return [[1]];


  const triangle = Array.from({ length: numRows }, () => {
    return Array.from({ length: 1 }, () => 1)
  });

  triangle[1].push(1);

  for (let i = 2; i < numRows; i += 1) {
    for (let j = 1; j < triangle[i - 1].length; j += 1) {
      const newEle = triangle[i - 1][j] + triangle[i - 1][j - 1];
      triangle[i].push(newEle)
    }
    triangle[i].push(1);
  }

  return triangle
};
