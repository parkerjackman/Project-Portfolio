public class Recursion {
    public static void main(String[] args) {

        int[] sumMe = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        System.out.printf("Array Sum: %d\n", arraySum(sumMe, 0));

        int[] minMe = { 0, 1, 1, 2, 3, 5, 8, -42, 13, 21, 34, 55, 89 };
        System.out.printf("Array Min: %d\n", arrayMin(minMe, 0));

        String[] amISymmetric =  {
                "You can cage a swallow can't you but you can't swallow a cage can you",
                "I still say cS 1410 is my favorite class"
        };
        for (String test : amISymmetric) {
            String[] words = test.toLowerCase().split(" ");
            System.out.println();
            System.out.println(test);
            System.out.printf("Is word symmetric: %b\n", isWordSymmetric(words, 0, words.length - 1));
        }

        double weights[][] = {
                { 51.18 },
                { 55.90, 131.25 },
                { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };
        System.out.println();
        System.out.println("--- Weight Pyramid ---");
        for (int row = 0; row < weights.length; row++) {
            for (int column = 0; column < weights[row].length; column++) {
                double weight = computePyramidWeights(weights, row, column);
                System.out.printf("%.2f ", weight);
            }
            System.out.println();
        }

        char image[][] = {
                {'*','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ','*','*',' ',' '},
                {' ','*',' ',' ','*','*','*',' ',' ',' '},
                {' ','*','*',' ','*',' ','*',' ','*',' '},
                {' ','*','*',' ','*','*','*','*','*','*'},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ','*','*','*',' ',' ','*',' '},
                {' ',' ',' ',' ',' ','*',' ',' ','*',' '}
        };
        int howMany = howManyOrganisms(image);
        System.out.println();
        System.out.println("--- Labeled Organism Image ---");
        for (char[] line : image) {
            for (char item : line) {
                System.out.print(item);
            }
            System.out.println();
        }
        System.out.printf("There are %d organisms in the image.\n", howMany);

    }

    public static boolean isWordSymmetric(String[] words, int start, int end){
        if (words.length == 0) { return true; }
        if (words.length == 1) { return true; }
        if (start == end) { return true; }
        if (start > end) { return false; }
        if (words[start].equalsIgnoreCase(words[end])) {
            isWordSymmetric(words, start + 1, end - 1);
            return true;
        } else {
            return false;
        }
    }

    public static long arraySum(int[] data, int position) {
        if (position >= data.length) {
            return 0;
        }
        if (data.length == 0) {
            return 0;
        }
        return (data[position] + arraySum(data, position + 1));
    }

    // wrapper
    public static int arrayMin(int[] data, int position) {
        return arrayMin(data, position,data[position]);
    }

//    helper
    public static int arrayMin(int[] data, int position, int currentMin) {
        if (position == data.length - 1) {
            return (data[position] < currentMin ? data[position] : currentMin);
        }
        else {
            currentMin = (data[position] < currentMin ? data[position] : currentMin);
            return arrayMin(data, position + 1, currentMin);
        }
    }

    public static double computePyramidWeights(double[][] weights, int row, int column) {
        if (row < 0 || column < 0) { return 0; }
        if (row >= weights.length || column >= weights[row].length) { return 0; }
        if (weights.length == 0 || weights[row].length == 0) { return 0; }

        return weights[row][column] + 0.5 * computePyramidWeights(weights, row - 1, column) + 0.5 * computePyramidWeights(weights, row - 1, column - 1);
    }

    // wrapper
    public static int howManyOrganisms(char[][] image) {
        int count = 0;
        char mark = 'a';
        int currentIndex = -1;
        for (int row = 0; row < image.length; row++) {
            for (int column = 0; column < image[row].length; column++) {
                if (image[row][column] == '*') {
                    markOrganism(image, row, column, mark);
                    count++;
                    mark++;
                }
            }
        }
        return count;
    }

    // helper
    public static void markOrganism(char[][] image, int row, int column, char letter) {
        if (row < 0 || row >= image.length){
            return;
        }
        if (column < 0 || column >= image[row].length) {
            return;
        }
        if (image[row][column] == '*') {
            image[row][column] = letter;
            if (row - 1 >= 0) {
                markOrganism(image, row - 1, column, letter);
            }
            if (row + 1 < image.length) {
                markOrganism(image, row + 1, column, letter);
            }
            if (column - 1 >= 0) {
                markOrganism(image, row, column - 1, letter);
            }
            if (column + 1 < image[row].length) {
                markOrganism(image, row, column + 1, letter);
            }
        }
    }
}
