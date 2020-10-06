import { sum, diff } from '../math';

describe('Examining the syntax of Jest tests', () => {
  test('sums numbers', () => {
    expect(sum(1, 2)).toStrictEqual(3);
    expect(sum(2, 2)).toStrictEqual(4);
  });

  test('diff numbers', () => {
    expect(diff(10, 5)).toStrictEqual(5);
    expect(diff(17, 6)).toStrictEqual(11);
  });
});
