
public class PatternPlane extends Pattern {
    private int sizeX = 5;
    private int sizeY = 4;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternPlane[y][x];
    }

    private boolean[][] patternPlane = {
            {false, false, true, false, false},
            {true, false, false, false, false},
            {true, false, true, true, true},
            {false, true, false, false, false}
    };

}