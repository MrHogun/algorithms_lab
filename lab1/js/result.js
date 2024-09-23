import { randomArray } from './utils/randomArray.js';
import { measureTime } from './utils/measureTime.js';
import { bubbleSort } from './algorithms/bublsort.js';
import { insertionSort } from './algorithms/insort.js';
import { quickSort } from './algorithms/hoare.js';

const sizes = [1000, 2000, 3000, 4000, 5000, 6000];

sizes.forEach(size => {
    const arr = randomArray(size);

    const bubbleTime = measureTime(bubbleSort, arr);
    const insertionTime = measureTime(insertionSort, arr);
    const quickTime = measureTime(quickSort, arr);

    console.log(`Array size: ${size}`);
    console.log(`Bubble Sort: ${bubbleTime.toFixed(2)} ms`);
    console.log(`Insertion Sort: ${insertionTime.toFixed(2)} ms`);
    console.log(`Quick Sort: ${quickTime.toFixed(2)} ms`);
    console.log('-----------------------------------');
});