#include <cassert>
#include <iostream>
#include "world.h"
#include "fishes.h"

int main() {
    // 1. Test boundaries
    World world(100, 50);
    assert(world.width() == 100);
    assert(world.height() == 50);
    assert(world.inside(10, 10, 5, 5) == true);
    assert(world.inside(-1, 10, 5, 5) == false);

    // 2. Test clear/flush
    assert(world.size() == 0);
    world.addEntity(std::make_unique<fish1>(100, 50));
    assert(world.size() == 1);
    world.clear();
    assert(world.size() == 0);

    std::cout << "All C++ unit tests passed!" << std::endl;
    return 0;
}
