import pyarrow
import dataclasses as dc

def _repr(self):
	if isinstance(self, pyarrow.Array):
		s = ', '.join(repr(v.as_py()) for v in self[:3])
		if len(self) > 3:
			s += ', ...'
		return f'[{s}]'
	elif isinstance(self, tuple):
		s = ', '.join(_repr(v) for v in self)
		return f'({s})'
	elif dc.is_dataclass(self):
		s = ', '.join(f'{f.name}={_repr(getattr(self, f.name))}' for f in dc.fields(type(self)))
		return f'{type(self).__name__}({s})'
	else:
		return repr(self)
