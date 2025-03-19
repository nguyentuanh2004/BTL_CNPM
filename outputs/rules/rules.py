def findDecision(obj): #obj[0]: Kỹ năng mềm, obj[1]: Đại số tuyến tính, obj[2]: Giải tích 1, obj[3]: Tin học đại cương, obj[4]: Vật lý điện từ, obj[5]: Giải tích 2, obj[6]: Lập trình nâng cao
	# {"feature": "L\u1eadp tr\u00ecnh n\u00e2ng cao", "instances": 683, "metric_value": 1.8503, "depth": 1}
	if obj[6] == 'D':
		# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 179, "metric_value": 1.551, "depth": 2}
		if obj[3] == 'C':
			# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 54, "metric_value": 1.3069, "depth": 3}
			if obj[4] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 18, "metric_value": 1.4153, "depth": 4}
				if obj[2] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Trung bình'
					elif obj[5] == 'D':
						return 'Khá'
					else: return 'Trung bình'
				elif obj[2] == 'C':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1] == 'A':
						return 'Khá'
					elif obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Khá'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[2] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[2] == 'A':
					return 'Khá'
				else: return 'Khá'
			elif obj[4] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[5] == 'C':
					return 'Khá'
				elif obj[5] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'F':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[5] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[5] == 'B':
					return 'Khá'
				else: return 'Khá'
			elif obj[4] == 'D':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 11, "metric_value": 1.3222, "depth": 4}
				if obj[5] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 1.371, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Trung bình'
					elif obj[2] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[5] == 'B':
					return 'Khá'
				elif obj[5] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[4] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[2] == 'C':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[2] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[4] == 'F':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[3] == 'B':
			# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 43, "metric_value": 1.4578, "depth": 3}
			if obj[5] == 'B':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 14, "metric_value": 1.2638, "depth": 4}
				if obj[4] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'A':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'A':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0] == 'C':
						return 'Khá'
					elif obj[0] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[4] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[5] == 'C':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 13, "metric_value": 1.2389, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[1] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[0] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'D':
						return 'Trung bình'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Trung bình'
				else: return 'Chưa Xếp Loại'
			elif obj[5] == 'D':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 11, "metric_value": 1.3222, "depth": 4}
				if obj[2] == 'C':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0] == 'B':
						return 'Khá'
					elif obj[0] == 'C':
						return 'Khá'
					elif obj[0] == 'D':
						return 'Khá'
					else: return 'Khá'
				elif obj[2] == 'D':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0] == 'C':
						return 'Khá'
					elif obj[0] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[2] == 'B':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[5] == 'A':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[1] == 'C':
					return 'Xuất sắc'
				else: return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[3] == 'A':
			# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 40, "metric_value": 1.5129, "depth": 3}
			if obj[1] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 16, "metric_value": 1.2476, "depth": 4}
				if obj[5] == 'C':
					return 'Khá'
				elif obj[5] == 'A':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 5, "metric_value": 1.5219, "depth": 5}
					if obj[4] == 'B':
						return 'Khá'
					elif obj[4] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[5] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[5] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[1] == 'D':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[2] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Khá'
					elif obj[4] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[2] == 'D':
					return 'Khá'
				elif obj[2] == 'B':
					return 'Khá'
				elif obj[2] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[1] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 8, "metric_value": 1.2988, "depth": 4}
				if obj[5] == 'A':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[4] == 'B':
						return 'Giỏi'
					elif obj[4] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[5] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[5] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[1] == 'A':
				return 'Giỏi'
			else: return 'Khá'
		elif obj[3] == 'D':
			# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 39, "metric_value": 1.3347, "depth": 3}
			if obj[5] == 'C':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 15, "metric_value": 0.9056, "depth": 4}
				if obj[0] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 9, "metric_value": 0.7642, "depth": 5}
					if obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'A':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[0] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[5] == 'B':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 12, "metric_value": 1.5, "depth": 4}
				if obj[4] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 7, "metric_value": 1.5567, "depth": 5}
					if obj[2] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'C':
						return 'Trung bình'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'B':
					return 'Khá'
				elif obj[4] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Trung bình'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[5] == 'D':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 9, "metric_value": 0.9864, "depth": 4}
				if obj[4] == 'D':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0] == 'A':
						return 'Trung bình'
					elif obj[0] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[0] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[4] == 'B':
					return 'Khá'
				elif obj[4] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[5] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2] == 'D':
					return 'Khá'
				elif obj[2] == 'A':
					return 'Chưa Xếp Loại'
				elif obj[2] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[3] == 'F':
			return 'Chưa Xếp Loại'
		else: return 'Chưa Xếp Loại'
	elif obj[6] == 'A':
		# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 178, "metric_value": 1.8303, "depth": 2}
		if obj[1] == 'B':
			# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 60, "metric_value": 1.7117, "depth": 3}
			if obj[2] == 'B':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 30, "metric_value": 1.4037, "depth": 4}
				if obj[4] == 'A':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 16, "metric_value": 1.0613, "depth": 5}
					if obj[0] == 'B':
						return 'Giỏi'
					elif obj[0] == 'A':
						return 'Giỏi'
					elif obj[0] == 'D':
						return 'Giỏi'
					elif obj[0] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[4] == 'B':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 9, "metric_value": 1.4355, "depth": 5}
					if obj[0] == 'B':
						return 'Giỏi'
					elif obj[0] == 'C':
						return 'Giỏi'
					elif obj[0] == 'A':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[4] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5] == 'A':
						return 'Khá'
					elif obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				else: return 'Giỏi'
			elif obj[2] == 'C':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 17, "metric_value": 1.7345, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 11, "metric_value": 1.2407, "depth": 5}
					if obj[4] == 'C':
						return 'Giỏi'
					elif obj[4] == 'A':
						return 'Giỏi'
					elif obj[4] == 'B':
						return 'Giỏi'
					elif obj[4] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[3] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'A':
						return 'Giỏi'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[3] == 'C':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[2] == 'A':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 12, "metric_value": 1.4591, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 5, "metric_value": 1.5219, "depth": 5}
					if obj[3] == 'A':
						return 'Giỏi'
					elif obj[3] == 'C':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[0] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5] == 'A':
						return 'Xuất sắc'
					elif obj[5] == 'B':
						return 'Khá'
					else: return 'Xuất sắc'
				elif obj[0] == 'C':
					return 'Giỏi'
				elif obj[0] == 'A':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[2] == 'D':
				return 'Chưa Xếp Loại'
			else: return 'Giỏi'
		elif obj[1] == 'A':
			# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 59, "metric_value": 1.7069, "depth": 3}
			if obj[4] == 'A':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 40, "metric_value": 1.6394, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 21, "metric_value": 1.5492, "depth": 5}
					if obj[3] == 'A':
						return 'Giỏi'
					elif obj[3] == 'B':
						return 'Giỏi'
					elif obj[3] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[0] == 'A':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 12, "metric_value": 1.325, "depth": 5}
					if obj[3] == 'A':
						return 'Xuất sắc'
					elif obj[3] == 'B':
						return 'Giỏi'
					elif obj[3] == 'C':
						return 'Giỏi'
					else: return 'Xuất sắc'
				elif obj[0] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'D':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[4] == 'B':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 14, "metric_value": 1.2871, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 13, "metric_value": 1.1401, "depth": 5}
					if obj[5] == 'A':
						return 'Giỏi'
					elif obj[5] == 'B':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[3] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Giỏi'
			elif obj[4] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 5, "metric_value": 1.371, "depth": 4}
				if obj[5] == 'B':
					return 'Khá'
				elif obj[5] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[5] == 'C':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Giỏi'
		elif obj[1] == 'C':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 46, "metric_value": 1.5069, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 18, "metric_value": 1.5305, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 8, "metric_value": 1.0613, "depth": 5}
					if obj[2] == 'B':
						return 'Giỏi'
					elif obj[2] == 'D':
						return 'Giỏi'
					elif obj[2] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[3] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 5, "metric_value": 1.5219, "depth": 5}
					if obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Giỏi'
					elif obj[4] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5] == 'D':
						return 'Khá'
					elif obj[5] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'D':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[0] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 14, "metric_value": 1.0949, "depth": 4}
				if obj[2] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 8, "metric_value": 1.0613, "depth": 5}
					if obj[4] == 'B':
						return 'Khá'
					elif obj[4] == 'A':
						return 'Khá'
					elif obj[4] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[2] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[2] == 'A':
					return 'Khá'
				elif obj[2] == 'D':
					return 'Khá'
				else: return 'Khá'
			elif obj[0] == 'D':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 9, "metric_value": 1.4355, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'A':
						return 'Giỏi'
					elif obj[4] == 'B':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[3] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'D':
					return 'Khá'
				elif obj[3] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[0] == 'A':
				return 'Giỏi'
			else: return 'Khá'
		elif obj[1] == 'D':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 13, "metric_value": 1.4605, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 7, "metric_value": 1.4488, "depth": 4}
				if obj[5] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[5] == 'A':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[0] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2] == 'B':
					return 'Khá'
				elif obj[2] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[0] == 'A':
				return 'Giỏi'
			elif obj[0] == 'D':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		else: return 'Giỏi'
	elif obj[6] == 'C':
		# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 169, "metric_value": 1.5993, "depth": 2}
		if obj[1] == 'D':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 54, "metric_value": 1.2897, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 24, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[5] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[3] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[3] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[0] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 20, "metric_value": 1.4577, "depth": 4}
				if obj[5] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[4] == 'D':
						return 'Khá'
					else: return 'Chưa Xếp Loại'
				elif obj[5] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 6, "metric_value": 1.4591, "depth": 5}
					if obj[2] == 'B':
						return 'Trung bình'
					elif obj[2] == 'D':
						return 'Trung bình'
					elif obj[2] == 'C':
						return 'Trung bình'
					else: return 'Trung bình'
				elif obj[5] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'C':
						return 'Khá'
					elif obj[2] == 'F':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'A':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[0] == 'D':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 7, "metric_value": 1.1488, "depth": 4}
				if obj[4] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5] == 'B':
						return 'Khá'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[4] == 'A':
					return 'Chưa Xếp Loại'
				elif obj[4] == 'D':
					return 'Trung bình'
				elif obj[4] == 'B':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[0] == 'A':
				return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[1] == 'C':
			# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 51, "metric_value": 1.2493, "depth": 3}
			if obj[4] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 17, "metric_value": 1.1596, "depth": 4}
				if obj[2] == 'C':
					return 'Khá'
				elif obj[2] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[5] == 'A':
						return 'Khá'
					elif obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'D':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Khá'
					else: return 'Khá'
				elif obj[2] == 'D':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'D':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[2] == 'A':
					# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[0] == 'A':
						return 'Giỏi'
					elif obj[0] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				else: return 'Khá'
			elif obj[4] == 'C':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 13, "metric_value": 1.2957, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5] == 'C':
						return 'Khá'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'C':
					return 'Khá'
				elif obj[0] == 'D':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[3] == 'C':
						return 'Giỏi'
					elif obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[3] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[4] == 'B':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[0] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'A':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'C':
						return 'Khá'
					elif obj[3] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[0] == 'D':
					return 'Chưa Xếp Loại'
				elif obj[0] == 'A':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[4] == 'D':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[0] == 'B':
					return 'Khá'
				elif obj[0] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[0] == 'C':
					return 'Khá'
				else: return 'Khá'
			elif obj[4] == 'F':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[1] == 'B':
			# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 35, "metric_value": 1.4544, "depth": 3}
			if obj[2] == 'B':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 13, "metric_value": 1.4196, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 7, "metric_value": 1.1488, "depth": 5}
					if obj[4] == 'B':
						return 'Khá'
					elif obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[0] == 'A':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'C':
						return 'Khá'
					elif obj[3] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[0] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'B':
						return 'Chưa Xếp Loại'
					elif obj[3] == 'C':
						return 'Giỏi'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[2] == 'C':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 13, "metric_value": 1.1401, "depth": 4}
				if obj[4] == 'A':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3] == 'B':
						return 'Khá'
					elif obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'D':
						return 'Khá'
					else: return 'Khá'
				elif obj[4] == 'C':
					return 'Khá'
				elif obj[4] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[5] == 'C':
						return 'Giỏi'
					elif obj[5] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[4] == 'F':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[2] == 'A':
				# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 6, "metric_value": 1.4591, "depth": 4}
				if obj[0] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'B':
						return 'Giỏi'
					elif obj[3] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[0] == 'C':
					return 'Khá'
				elif obj[0] == 'A':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[2] == 'D':
				return 'Chưa Xếp Loại'
			else: return 'Khá'
		elif obj[1] == 'A':
			# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 28, "metric_value": 1.8288, "depth": 3}
			if obj[0] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 12, "metric_value": 1.5546, "depth": 4}
				if obj[5] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2] == 'B':
						return 'Giỏi'
					elif obj[2] == 'A':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[5] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[5] == 'D':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'C':
					return 'Khá'
				else: return 'Khá'
			elif obj[0] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 8, "metric_value": 1.4056, "depth": 4}
				if obj[5] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[5] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'D':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'A':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[0] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[5] == 'A':
					return 'Giỏi'
				elif obj[5] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'D':
						return 'Giỏi'
					elif obj[4] == 'A':
						return 'Xuất sắc'
					else: return 'Giỏi'
				elif obj[5] == 'C':
					return 'Xuất sắc'
				else: return 'Giỏi'
			elif obj[0] == 'D':
				return 'Khá'
			else: return 'Khá'
		elif obj[1] == 'F':
			return 'Chưa Xếp Loại'
		else: return 'Khá'
	elif obj[6] == 'B':
		# {"feature": "K\u1ef9 n\u0103ng m\u1ec1m", "instances": 141, "metric_value": 1.7622, "depth": 2}
		if obj[0] == 'B':
			# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 67, "metric_value": 1.6165, "depth": 3}
			if obj[1] == 'C':
				# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 24, "metric_value": 1.4171, "depth": 4}
				if obj[4] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 9, "metric_value": 1.585, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[2] == 'D':
						return 'Giỏi'
					elif obj[2] == 'A':
						return 'Khá'
					else: return 'Giỏi'
				elif obj[4] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Khá'
					elif obj[3] == 'D':
						return 'Khá'
					elif obj[3] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[4] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[4] == 'D':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[5] == 'D':
						return 'Khá'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'A':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[1] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 18, "metric_value": 1.4807, "depth": 4}
				if obj[2] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 11, "metric_value": 1.3222, "depth": 5}
					if obj[5] == 'B':
						return 'Khá'
					elif obj[5] == 'A':
						return 'Giỏi'
					elif obj[5] == 'C':
						return 'Giỏi'
					elif obj[5] == 'D':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[2] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'D':
						return 'Khá'
					elif obj[4] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[2] == 'A':
					return 'Giỏi'
				elif obj[2] == 'D':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			elif obj[1] == 'A':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 15, "metric_value": 1.4295, "depth": 4}
				if obj[3] == 'B':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4] == 'A':
						return 'Khá'
					elif obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'B':
						return 'Giỏi'
					else: return 'Khá'
				elif obj[3] == 'A':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 5, "metric_value": 1.371, "depth": 5}
					if obj[5] == 'A':
						return 'Giỏi'
					elif obj[5] == 'B':
						return 'Giỏi'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[3] == 'D':
					return 'Giỏi'
				elif obj[3] == 'C':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'B':
						return 'Giỏi'
					elif obj[4] == '0':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				else: return 'Giỏi'
			elif obj[1] == 'D':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 10, "metric_value": 1.2955, "depth": 4}
				if obj[5] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[5] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[3] == 'D':
						return 'Trung bình'
					elif obj[3] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[5] == 'D':
					return 'Khá'
				elif obj[5] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[0] == 'C':
			# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 35, "metric_value": 1.2076, "depth": 3}
			if obj[4] == 'C':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[3] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[2] == 'D':
						return 'Khá'
					elif obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[1] == 'B':
						return 'Khá'
					elif obj[1] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[3] == 'D':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'C':
						return 'Khá'
					elif obj[1] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[3] == 'C':
					return 'Khá'
				else: return 'Khá'
			elif obj[4] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 9, "metric_value": 1.2244, "depth": 4}
				if obj[2] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'C':
						return 'Giỏi'
					elif obj[3] == 'D':
						return 'Khá'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[2] == 'C':
					return 'Khá'
				elif obj[2] == 'A':
					return 'Giỏi'
				else: return 'Khá'
			elif obj[4] == 'D':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3] == 'B':
					# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[5] == 'B':
						return 'Khá'
					elif obj[5] == 'A':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'D':
						return 'Chưa Xếp Loại'
					elif obj[5] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[3] == 'C':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Khá'
					else: return 'Khá'
				elif obj[3] == 'A':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			elif obj[4] == 'B':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3] == 'B':
						return 'Khá'
					elif obj[3] == 'A':
						return 'Khá'
					elif obj[3] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[1] == 'B':
					return 'Chưa Xếp Loại'
				elif obj[1] == 'D':
					return 'Khá'
				else: return 'Khá'
			else: return 'Khá'
		elif obj[0] == 'D':
			# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 23, "metric_value": 1.3709, "depth": 3}
			if obj[1] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[2] == 'C':
					return 'Chưa Xếp Loại'
				elif obj[2] == 'B':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'C':
						return 'Trung bình'
					elif obj[3] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Trung bình'
				else: return 'Chưa Xếp Loại'
			elif obj[1] == 'B':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 6, "metric_value": 1.2516, "depth": 4}
				if obj[2] == 'D':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'D':
						return 'Trung bình'
					elif obj[3] == 'C':
						return 'Khá'
					else: return 'Trung bình'
				elif obj[2] == 'B':
					return 'Khá'
				elif obj[2] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'C':
						return 'Khá'
					else: return 'Khá'
				else: return 'Khá'
			elif obj[1] == 'A':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2] == 'D':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'C':
						return 'Khá'
					elif obj[4] == 'D':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[2] == 'C':
					# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[3] == 'A':
						return 'Khá'
					else: return 'Khá'
				elif obj[2] == 'A':
					return 'Chưa Xếp Loại'
				else: return 'Chưa Xếp Loại'
			elif obj[1] == 'D':
				# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[5] == 'D':
					# {"feature": "V\u1eadt l\u00fd \u0111i\u1ec7n t\u1eeb", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'D':
						return 'Trung bình'
					elif obj[4] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Chưa Xếp Loại'
				elif obj[5] == 'C':
					return 'Khá'
				else: return 'Chưa Xếp Loại'
			else: return 'Chưa Xếp Loại'
		elif obj[0] == 'A':
			# {"feature": "Gi\u1ea3i t\u00edch 2", "instances": 16, "metric_value": 1.8802, "depth": 3}
			if obj[5] == 'C':
				# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 7, "metric_value": 1.5567, "depth": 4}
				if obj[2] == 'B':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[1] == 'A':
						return 'Giỏi'
					elif obj[1] == 'B':
						return 'Chưa Xếp Loại'
					else: return 'Giỏi'
				elif obj[2] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'D':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[2] == 'C':
					return 'Giỏi'
				elif obj[2] == 'D':
					return 'Khá'
				else: return 'Giỏi'
			elif obj[5] == 'A':
				# {"feature": "Tin h\u1ecdc \u0111\u1ea1i c\u01b0\u01a1ng", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'A':
					# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1] == 'A':
						return 'Xuất sắc'
					elif obj[1] == 'B':
						return 'Giỏi'
					elif obj[1] == 'C':
						return 'Giỏi'
					else: return 'Giỏi'
				elif obj[3] == 'B':
					return 'Giỏi'
				else: return 'Giỏi'
			elif obj[5] == 'B':
				# {"feature": "\u0110\u1ea1i s\u1ed1 tuy\u1ebfn t\u00ednh", "instances": 3, "metric_value": 1.585, "depth": 4}
				if obj[1] == 'C':
					# {"feature": "Gi\u1ea3i t\u00edch 1", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2] == 'B':
						return 'Khá'
					elif obj[2] == 'C':
						return 'Chưa Xếp Loại'
					else: return 'Khá'
				elif obj[1] == 'A':
					return 'Xuất sắc'
				else: return 'Khá'
			else: return 'Giỏi'
		else: return 'Khá'
	elif obj[6] == 'F':
		return 'Chưa Xếp Loại'
	else: return 'Khá'
