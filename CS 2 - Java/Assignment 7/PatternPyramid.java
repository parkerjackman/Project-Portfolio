
public class PatternPyramid extends Pattern {
    private int sizeX = 5;
    private int sizeY = 3;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternPyramid[y][x];
    }

    private boolean[][] patternPyramid = {
            {false, false, true, false, false},
            {false, true, true, true, false},
            {true, false, false, false, true}
    };

}