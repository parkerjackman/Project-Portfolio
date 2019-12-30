/**
 * Assignment 3 for CS 1410
 * This program determines if points are contained within circles or rectangles.
 */
public class Inside {
    /**
     * This is the primary driver code to test the "inside" capabilities of the
     * various functions.
     */
    public static void main(String[] args) {
        double[] ptX = {1, 2, 3, 4};
        double[] ptY = {1, 2, 3, 4};
        double[] circleX = {0, 5};
        double[] circleY = {0, 5};
        double[] circleRadius = {3, 3};
        double[] rectLeft = {-2.5, -2.5};
        double[] rectTop = {2.5, 5.0};
        double[] rectWidth = {6.0, 5.0};
        double[] rectHeight = {5.0, 2.5};

        System.out.println("--- Report of Points and Circles ---");
        System.out.println();

        for (int currentCircle = 0; currentCircle < circleX.length; currentCircle++) {

            for (int currentPoint = 0; currentPoint < ptX.length; currentPoint++) {
                if (isPointInsideCircle(ptX[currentPoint], ptY[currentPoint], circleX[currentCircle], circleY[currentCircle], circleRadius[currentCircle])) {
                    reportPoint(ptX[currentPoint], ptY[currentPoint]);
                    System.out.print(" is inside ");
                    reportCircle(circleX[currentCircle], circleY[currentCircle], circleRadius[currentCircle]);
                }
                else {
                    reportPoint(ptX[currentPoint], ptY[currentPoint]);
                    System.out.print(" is outside ");
                    reportCircle(circleX[currentCircle], circleY[currentCircle], circleRadius[currentCircle]);
                }
                System.out.println();
            }
        }
        System.out.println();

        System.out.println("--- Report of Points and Rectangles ---");
        System.out.println();

        for (int currentRectangle = 0; currentRectangle < rectLeft.length; currentRectangle++){

            for (int currentPoint = 0; currentPoint < ptX.length; currentPoint++) {
                //left, top, width, height

                if (isPointInsideRectangle(ptX[currentPoint], ptY[currentPoint], rectLeft[currentRectangle], rectTop[currentRectangle], rectWidth[currentRectangle], rectHeight[currentRectangle])) {
                    reportPoint(ptX[currentPoint], ptY[currentPoint]);
                    System.out.print(" is inside ");
                    reportRectangle(rectLeft[currentRectangle], rectTop[currentRectangle], rectWidth[currentRectangle], rectHeight[currentRectangle]);
                }
                else {
                    reportPoint(ptX[currentPoint], ptY[currentPoint]);
                    System.out.print(" is outside ");
                    reportRectangle(rectLeft[currentRectangle], rectTop[currentRectangle], rectWidth[currentRectangle], rectHeight[currentRectangle]);
                }
                System.out.println();
            }
        }
    }

    // Prints the details for a single point. Ex: Point (1.0, 1.0)
    static void reportPoint(double x, double y){
        System.out.print("Point(" + x + ", " + y + ")");
    }

    // Prints the details for a single circle. Ex: Circle (0.0, 0.0) Radius: 3.0
    static void reportCircle(double x, double y, double r){
        System.out.print("Circle(" + x + ", " + y + ") Radius: " + r);
    }

    // Prints the details for a single rectangle.
    // It should show the left, top, right, and bottom values.
    static void reportRectangle(double left, double top, double width, double height) {
        double right = left + width;
        double bottom = top - height;
        System.out.print("Rectanlge(" + left + ", " + top + ", " + right + ", " + bottom + ")");

    }

    //Tests if a point is inside a circle
    //points on the edge of a circle are considered inside
    static boolean isPointInsideCircle(double ptX, double ptY, double circleX, double circleY, double circleRadius){
        double differenceX = ptX - circleX;
        double differenceY = ptY - circleY;
        double distance = Math.sqrt(Math.pow(differenceX, 2) + Math.pow(differenceY, 2));
        boolean isInsideCircle = distance <= circleRadius;

        return isInsideCircle;
    }

    // Tests if a point is inside a rectangle
    // points on the edge of a rectangle are considered inside
    static boolean isPointInsideRectangle(double ptX, double ptY, double rLeft, double rTop, double rWidth, double rHeight){
        boolean isInsideLeftRight = rLeft <= ptX && ptX <= (rLeft + rWidth);
        boolean isInsideTopBottom = (rTop - rHeight) <= ptY && ptY <= rTop;
        boolean isInsideRectangle = isInsideLeftRight && isInsideTopBottom;

        return isInsideRectangle;
    }
}

