class moon {
    public:
        int pos[3];
        int vel[3] = {0,0,0};

        moon(int startX, int startY, int startZ);

        void calcVelocity(moon other);
        void calcPosition();

        int getEnergy();
};