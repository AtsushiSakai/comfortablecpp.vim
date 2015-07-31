

struct Sample{
  int a;
  float b;
  double c;
};


void ShowSamplestruct(const Sample &obj){
	printf("__func__");
	printf("a:%d\n");
	printf("b:%f\n");
	printf("c:%lf\n");
}

