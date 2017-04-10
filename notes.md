`inputs.2d`:

- `amr.max_level  (when this = 0 points to no refinement and = # allows for #+1 levels).`
- `stop_time`

`probin`:

```yaml
&tagging
     dengrad = (tagging criterion for when density changes, at what value of the gradient of density should we tag for refinement)
     dengrad_max_level = (how many levels of refinement can we reach through the density gradient criterion, this must be <= your amr.max_level)
/
```

- a text file describing your choice of refinement criteria

- generates
	- png without annotation
	- png with annotation
