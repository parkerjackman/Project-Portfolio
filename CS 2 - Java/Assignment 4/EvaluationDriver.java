/**
 * Assignment 4 for CS 1410
 * This program evaluates the linear and binary searching, along
 * with comparing performance difference between the selection sort
 * and the built-in java.util.Arrays.sort.
 *
 * @author
 */
public class EvaluationDriver {
    static final int MAX_VALUE = 1_000_000;
    static final int MAX_ARRAY_SIZE = 100_000;
    static final int ARRAY_INCREMENT = 20_000;
    static final int NUMBER_SEARCHES = 50_000;

    public static void main(String[] args) {

        demoLinearSearchUnsorted();
        demoLinearSearchSorted();
        demoBinarySearchSelectionSort();
        demoBinarySearchFastSort();
    }

    /**
     * Demonstrates linear searching over an unsorted array
     *
     */
    public static void demoLinearSearchUnsorted() {
        System.out.println("--- Linear Search Timing (Unsorted) ---");

        for (int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i += ARRAY_INCREMENT) {
            int count = 0;
            int[] array = generateNumbers(i, MAX_VALUE);
            long start = System.currentTimeMillis();

            for (int j = 0; j < NUMBER_SEARCHES; j++) {
                int value = (int)(Math.random() * MAX_VALUE);

                if (linearSearch(array, value)) {
                    count++;
                }
            }

            long end = System.currentTimeMillis();
            long timeTook = end - start;

            System.out.println("Number of items       : " + i);
            System.out.println("Times value was found : " + count);
            System.out.println("Total search time     : " + timeTook + " ms");
            System.out.println();
        }
    }

    /**
     * Demonstrates linear searching over a sorted array
     *
     */
    public static void demoLinearSearchSorted() {
        System.out.println("--- Linear Search Timing (Sorted) ---");

        for (int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i += ARRAY_INCREMENT) {
            int count = 0;
            int[] array = generateNumbers(i, MAX_VALUE);
            long start = System.currentTimeMillis();
            selectionSort(array);

            for (int j = 0; j < NUMBER_SEARCHES; j++) {
                int value = (int)(Math.random() * MAX_VALUE);

                if (linearSearch(array, value)) {
                    count++;
                }
            }

            long end = System.currentTimeMillis();
            long timeTook = end - start;

            System.out.println("Number of items       : " + i);
            System.out.println("Times value was found : " + count);
            System.out.println("Total search time     : " + timeTook + " ms");
            System.out.println();
        }
    }


    /**
     * Demonstrates binary searching when using a Selection Sort
     *
     */
    public static void demoBinarySearchSelectionSort() {
        System.out.println("--- Binary Search Timing (Selection Sort) ---");

        for (int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i += ARRAY_INCREMENT) {
            int count = 0;
            int[] array = generateNumbers(i, MAX_VALUE);
            long start = System.currentTimeMillis();
            selectionSort(array);

            for (int j = 0; j < NUMBER_SEARCHES; j++) {
                int value = (int)(Math.random() * MAX_VALUE);

                if (binarySearch(array, value)) {
                    count++;
                }
            }

            long end = System.currentTimeMillis();
            long timeTook = end - start;

            System.out.println("Number of items       : " + i);
            System.out.println("Times value was found : " + count);
            System.out.println("Total search time     : " + timeTook + " ms");
            System.out.println();
        }
    }


    /**
     * Demonstrates binary searching when using the build in Arrays.sort
     *
     */
    public static void demoBinarySearchFastSort() {
        System.out.println("--- Binary Search Timing (arrays.sort) ---");

        for (int i = ARRAY_INCREMENT; i <= MAX_ARRAY_SIZE; i += ARRAY_INCREMENT) {
            int count = 0;
            int[] array = generateNumbers(i, MAX_VALUE);
            long start = System.currentTimeMillis();
            java.util.Arrays.sort(array);


            for (int j = 0; j < NUMBER_SEARCHES; j++) {
                int value = (int)(Math.random() * MAX_VALUE);
                if (binarySearch(array, value)) {
                    count++;
                }
            }

            long end = System.currentTimeMillis();
            long timeTook = end - start;
            System.out.println("Number of items       : " + i);
            System.out.println("Times value was found : " + count);
            System.out.println("Total search time     : " + timeTook + " ms");
            System.out.println();
        }
    }


    // Building Block methods

    public static int[] generateNumbers(int howMany, int maxValue){
        if (howMany > 0) {
            int[] randomArray = new int[howMany];
            for (int i = 0; i < howMany; i++) {
                randomArray[i] = (int) (Math.random() * maxValue);
            }
            return randomArray;
        }
        return null;
    }

    public static boolean linearSearch(int[] data, int search){
        boolean foundValue = false;
        for (int i = 0; i < data.length; i++) {
            if (search == data[i]) {
                foundValue = true;
            }
        }
        return foundValue;
    }

    public static boolean binarySearch(int[] data, int search){
        int low = 0;
        int high = data.length - 1;
        boolean foundValue = false;
        while (high >= low) {
            int mid = (low + high) / 2;
            if (search < data[mid]) {
                high = mid - 1;
            }
            else if (search == data[mid]) {
                foundValue = true;
                return foundValue;
            }
            else {
                low = mid + 1;
            }
        }
        return foundValue;
    }

    public static void selectionSort(int[] data){
        for (int i = 0; i < data.length - 1; i++) {
            int currentMin = data[i];
            int currentMinIndex = i;
            for (int j = i + 1; j < data.length; j++) {
                if (currentMin > data[j]) {
                    currentMin = data[j];
                    currentMinIndex = j;
                }
            }

            if (currentMinIndex != i) {
                data[currentMinIndex] = data[i];
                data[i] = currentMin;
            }
        }
    }
}
