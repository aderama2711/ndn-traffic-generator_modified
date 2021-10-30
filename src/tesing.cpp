#include "discrete_distribution.h"
#include "discrete_distribution_ii.h"
#include "zipf-mandelbrot.h"

int main(){
	int count[100];
	int i =0;
	for(i=0;i<1000;i++){
	  static rng::zipf_mandelbrot_distribution<rng::discrete_distribution_30bit,int> trafficDistZipf(0.8, 0, 100);
      trafficKey = trafficDistZipf(random::getRandomNumberEngine());
      count[i]++;
	}
}
