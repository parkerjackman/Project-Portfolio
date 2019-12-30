
public class PatternGlider extends Pattern {
    private int sizeX = 3;
    private int sizeY = 3;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternGlider[y][x];
    }

    private boolean[][] patternGlider = {
            {false, true, false},
            {false, false, true},
            {true, true, true}

    };
}