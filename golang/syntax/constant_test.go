package constant_test

import (
	"testing"
)

func TestConstant(t *testing.T) {
	const (
		a = 1 << iota
		b
		c
		d
	)
	constantArray := [...]int{a, b, c, d}
	for i, v := range constantArray {
		t.Logf("the index is %d, the base 10 value: %d, the base 2 value: %b", i, v, v)
	}
}
