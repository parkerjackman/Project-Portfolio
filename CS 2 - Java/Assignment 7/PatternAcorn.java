
public class PatternAcorn extends Pattern {
    private int sizeX = 7;
    private int sizeY = 3;

    public int getSizeX() {
        return sizeX;
    }
    public int getSizeY() {
        return sizeY;
    }
    public boolean getCell(int x, int y) {
        return patternAcorn[y][x];
    }

    private boolean[][] patternAcorn = {
            {false, true, false, false, false, false, false},
            {false, false, false, true, false, false, false},
            {true, true, false, false, true, true, true}
    };

}