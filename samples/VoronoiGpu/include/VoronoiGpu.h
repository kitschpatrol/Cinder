#pragma once
#include "cinder/Surface.h"
#include "cinder/Vector.h"

#include <vector>

ci::Surface32f calcDiscreteVoronoiGpu( const std::vector<ci::ivec2> &points, int width, int height );
ci::Channel32f calcDistanceMapGpu( const std::vector<ci::ivec2> &points, int width, int height );