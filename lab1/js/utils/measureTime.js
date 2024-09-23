export function measureTime(fn, arr) {
    const start = performance.now();
    fn([...arr]); 
    return performance.now() - start;
}