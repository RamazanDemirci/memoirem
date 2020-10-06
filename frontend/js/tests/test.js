import { sum, diff } from '../math';

describe('Examining the syntax of Jest tests', () => {

    it('sums numbers', () => {
        expect(sum(1, 2)).toEqual(3);
        expect(sum(2, 2)).toEqual(4);
    });

    it('diff numbers', () => {
        expect(diff(10, 5)).toEqual(5);
        expect(diff(17, 6)).toEqual(11);
    });
});