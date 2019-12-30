import java.util.Scanner;

public class Pyramid2 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Enter the number of lines: ");
        int numLines = input.nextInt();
        int largestNum = (int)Math.pow(2, numLines - 1);
        int numDigits = 0;
        while (largestNum > 0) {
            largestNum = largestNum / 10;
            numDigits++;
        }

        int minWidth = numDigits + 1;
        String standardFormat = "%" + minWidth + "d";

        int firstWidth = (numLines * minWidth) + minWidth;

        for (int currentNum = 1; currentNum <= numLines; currentNum++) {
            firstWidth -= minWidth;
            String pivotFormat = "%n%" + firstWidth + "d";
            int pivot = 1;
            System.out.printf(pivotFormat, pivot);

            for (int multiply = pivot * 2; multiply <= (int)Math.pow(2, currentNum - 1); multiply *= 2){
                System.out.printf(standardFormat, multiply);
            }

            for (int divide = (int)Math.pow(2, currentNum - 1) / 2; divide >= 1; divide /= 2){
                System.out.printf(standardFormat, divide);
            }
        }
    }
}